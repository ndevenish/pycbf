#!/bin/bash

set -eu

R="$(printf "\033[31m")"
W="$(printf "\033[37m")"
M="$(printf "\033[35m")"
NC="$(printf "\033[0m")"
BOLD="$(printf "\033[1m")"

print_usage() {
    echo "Usage: $0 [-h|--help] [--no-tag] ARG [ARG...]"
}
print_help() {
    print_usage
    echo
    echo "Create release commits and tags, including regeneration"
    echo
    echo "-h, --help      Show this message"
    echo "--no-tag        Don't create a tag for the release commit"
#    echo "--dry-run, -n   Don't do anything"
    echo
    echo "ARG....      Arguments to pass to bump2version"
}
quietly() {
    printf $W
    if ! "$*" | sed 's/\x1b\[[0-9;]*m//g'; then
        return 1
    fi
}

DRY_RUN=""
ALLOW_NONMAIN=""
ALLOW_DIRTY=""
NO_TAG=""
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
        *)
            _positionals+=("$1")
            ;;
    esac
    shift
done

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
_start_commit="$(git rev-parse HEAD)"

echo "Starting release process"
bump2version_args=(release --list)
if [[ $ALLOW_DIRTY == true ]]; then
    bump2version_args+=(--allow-dirty)
fi
if ! _output="$(set -x; bump2version "${bump2version_args[@]}")"; then
    echo "${R}Error: Bump2version failed"
    echo "$_output" $NC
fi
echo "$W$_output$NC"

new_version="$(echo "$_output" | grep new_version | sed -r s,"^.*=",,)"
echo "New version: $BOLD$M$new_version$NC"

echo "Regenerating SWIG files$W"
(set -x; ./regenerate_pycbf.py)

echo "${NC}Re-running build for Cython$W"
quietly (set -x; poetry build 2>&1)

echo "${NC}Running pre-commit to clean up$W"
quietly (set -x; pre-commit run --all 2>&1) || true

echo "${NC}Running towncrier$W"
quietly towncrier --yes

echo "${NC}Making commit$W"
