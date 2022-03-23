#!/bin/bash


PY_VERSIONS=(3.8 3.9 3.10)


# Safety catch to prevent people just running
if [[ $# -ne 2 || $1 == "-h" || $1 == "--help" ]]; then
    echo -e "Usage: build_many_locally.sh <version> <output_directory>

Bare-basics utility script to build MacOS-arm pypi packages from a local
machine, as there aren't native Apple Silicon runners in GitHub Actions
yet, and cross-compilation doesn't work in cibuildwheel because poetry
doesn't name the output wheels correctly.

Arguments:
    <version>           The version of pycbf to build.
    <output_directory>  The location to do intermediate build folders
                        and place the eventual wheel files."
    exit 1
fi

if [[ ! -d "$2" ]]; then
    if ! mkdir "$2"; then
        echo "Error: Destination directory '$2' does not exist and cannot create"
        exit 1
    fi
    cd "$2"
else
    cd "$2"
fi
DIR="$(pwd)"

eval "$(conda shell.bash hook)"

set -eu

# Extract the version from pyproject.toml
VERSION="$1"
echo -e "Running build for pycbf \033[1m$VERSION\033[0m]"

echo "Fetching sdist"
set -x

curl -L https://pypi.io/packages/source/p/pycbf/pycbf-${VERSION}.tar.gz \
    > "$DIR/pycbf-${VERSION:?}.tar.gz"

for ver in "${PY_VERSIONS[@]}"; do
    flatver="$(echo $ver | sed 's/\.//')"
    echo "Doing $ver"
    cd "$DIR"
    sleep 3
    mamba create -yp "ENV_$ver/" "python=$ver"
    set +eux
    conda activate "ENV_$ver/"
    set -eux
    mkdir build_$ver
    cd build_$ver
    tar -xf "$DIR/pycbf-${VERSION}.tar.gz" --strip-components=1
    # On mac, numpy isn't installable as a wheel. Remove for the build, which doesn't use
    cp pyproject.toml pyproject.toml.bak
    sed -i'' -e 's/numpy = ">=1.17"/# numpy = ">=1.17"/' pyproject.toml
    poetry env use python$ver
    poetry install
    # Undo the numpy removal so the metadata is correct
    mv pyproject.toml.bak pyproject.toml
    poetry build -f wheel
    mv dist/*.whl $DIR/pycbf-${VERSION}-cp$flatver-cp$flatver-macosx_11_0_arm64.whl
    mkdir -p "$DIR/unzip/$ver"
    cd "$DIR/unzip/$ver"
    unzip "$DIR/pycbf-${VERSION}-cp$flatver-cp$flatver-macosx_11_0_arm64.whl"
done

set +x
echo "Output:"
tree "$DIR/unzip"
echo "Wheels:"
ls "$DIR/*.whl"