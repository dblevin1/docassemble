#!/usr/bin/bash

function stopfunc {
    if [ -d ".git" ]; then
        echo "Stopping, changing branch"
        git checkout $current_branch
    fi
    exit 0
}

trap stopfunc SIGINT SIGTERM

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd $SCRIPT_DIR

if [ ! -z "$(git status -s)" ]; then
    echo "----EXITING, uncommitted changes found-----"
    exit
fi

current_branch=$(git branch --show-current)
git fetch origin
git fetch upstream
git checkout --detach upstream/master
doc_version=$(git describe --tags --abbrev=0)
echo "Using version $doc_version"
git checkout tags/$doc_version -B upstream-latest
git checkout $current_branch
echo "Branch 'upstream-latest' is now up to date"
