#!/bin/bash

set -eu

R="$(printf "\033[31m")"
B="$(printf "\033[34m")"
W="$(printf "\033[37m")"
M="$(printf "\033[35m")"
NC="$(printf "\033[0m")"
BOLD="$(printf "\033[1m")"

print_usage() {
    echo "Usage: $0 [-h|--help] [--no-tag] [--no-edit] --do"
}
print_help() {
    print_usage
    echo
    echo "Create release commits and tags, including regeneration"
    echo
    echo "-h, --help      Show this message"
    echo "--no-tag        Don't create a tag for the release commit"
    echo "--no-edit       Don't pause to allow CHANGELOG editing"
    echo "--do            Actually run. Safety so that no arguments doesnt commit"
#    echo "--dry-run, -n   Don't do anything"
    echo
    echo "ARG....      Arguments to pass to bump2version"
}
quietly() {
    echo "${W}+ $@"
    if ! "$@" 2>&1 | sed 's/\x1b\[[0-9;]*m//g'; then
        printf $NC
        return 1
    fi
    printf $NC
}

silently() {
    echo "${W}+ $@$NC"
    if ! _output="$("$@" 2>&1)"; then
        echo "${R}Error:"
        echo "$_output" | sed 's/\x1b\[[0-9;]*m//g'
        printf $NC
        return 1
    fi
}

DRY_RUN=""
ALLOW_NONMAIN=""
ALLOW_DIRTY=""
NO_TAG=""
NO_EDIT=""
DO=""
_positionals=()
while [[ $# -gt 0 ]]; do
    _key="$1"
    case "$_key" in
        -h|--help)
            print_help
            exit 0
            ;;
        -h*)
            print_help
            exit 0
            ;;
        -n|--dry-run)
            DRY_RUN=true
            ;;
        --allow-nonmain)
            ALLOW_NONMAIN=true
            ;;
        --allow-dirty)
            ALLOW_DIRTY=true
            ;;
        --no-tag)
            NO_TAG=true
            ;;
        --no-edit)
            NO_EDIT=true
            ;;
        --do)
            DO=true
            ;;
        *)
            _positionals+=("$1")
            ;;
    esac
    shift
done

if [[ ${#_positionals[@]} -gt 0 ]]; then
    echo "${R}Error: Unknown positional arguments: ${_positionals[@]}"
    exit 1
fi

if [[ $DO != true ]]; then
    print_usage
    echo "${R}Error: You must pass --do to actually make a release$NC"
    exit 1
fi

if [[ $DRY_RUN == true ]]; then
    echo "Error: Sorry, dry-run isn't implemented yet"
    exit 1
fi

# Verify we are on main
if [[ $ALLOW_NONMAIN != true && "$(git rev-parse --abbrev-ref HEAD)" != "main" ]]; then
    echo "${R}Error: Not on branch ${BOLD}main${NC}${R}, cannot make release"
    exit 1
fi

# Check we aren't dirty
if [[ $ALLOW_DIRTY != true && -n "$(git status --porcelain | grep -v '??')" ]]; then
    echo "${R}Error: Working branch is dirty. Cannot continue."
    exit 1
fi

# Check that _this file_ isn't dirty
if [[ -n "$(git status --porcelain | grep make_release.sh)" ]]; then
    echo "${R}Fatal Error: Release generation file make_release.sh is dirty$NC"
    exit
fi
_start_commit="$(git rev-parse HEAD)"

echo "Starting release process"
bump2version_args=(release --list)
if [[ $ALLOW_DIRTY == true ]]; then
    bump2version_args+=(--allow-dirty)
fi
if ! _output="$(set -x; bump2version "${bump2version_args[@]}")"; then
    echo "${R}Error: Bump2version failed"
    echo "$_output" $NC
    exit 1
fi

new_version="$(echo "$_output" | grep new_version | sed -r s,"^.*=",,)"
echo "New version: $BOLD$M$new_version$NC"

echo "Regenerating SWIG files$W"
silently ./regenerate_pycbf.py

echo "Removing numpy from dependencies"
silently cp pyproject.toml pyproject.toml.bak
silently sed -i'' -e 's/numpy = ">=1.17"/# numpy = ">=1.17"/' pyproject.toml

echo "Installing base environment"
silently poetry install

echo "Restoring original package"
silently mv pyproject.toml.bak pyproject.toml

echo "Re-running build for Cython"
silently poetry build

echo "Running towncrier"
silently towncrier --yes --version="$new_version"

if [[ $NO_EDIT != true ]]; then
    echo "Pausing for CHANGELOG editing"
    ${EDITOR:-vi} CHANGELOG.rst
else
    echo "No editing phase requested; using CHANGELOG as-is"
fi

echo "Running pre-commit to clean up"
quietly pre-commit run --all || true


echo "${BOLD}Making commit$NC"
quietly git add --update
quietly git commit -n -m "pycbf $new_version"

if [[ $NO_TAG != "true" ]]; then
    echo "Making tag ${M}v${new_version}$NC"
    quietly git tag "v${new_version}"
fi

echo "$NC"
echo "Advancing to new development release"

if ! _output="$(set -x; bump2version minor --list)"; then
    echo "${R}Error: Advancing release tag to next development release"
    echo "$_output" $NC
    exit 1
fi

new_dev_version="$(echo "$_output" | grep new_version | sed -r s,"^.*=",,)"
echo "New development version: $BOLD$M$new_dev_version$NC"

echo "Regenerating SWIG files$W"
silently ./regenerate_pycbf.py

echo "Re-running build for Cython"
silently poetry build

echo "${BOLD}Making new development commit$NC"
(   set -x
    git add --update
    git commit -n -m "Advance to ${new_dev_version} development series"
)
echo
echo "Successfully released $M$new_version$NC and advanced to $M$new_dev_version$NC"
echo
if [[ $NO_TAG != true ]]; then
    echo "Please remember to ${B}git push --tags$NC"
fi
