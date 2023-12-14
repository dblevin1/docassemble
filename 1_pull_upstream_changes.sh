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
doc_version_hash=$(git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' upstream | tail --lines=1 | sed -E "s/\s+.*//")
doc_version=$(git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' upstream | tail --lines=1 | sed -E "s/.*\s*.*v//" | sed "s/\^{}//")
echo "Using version $doc_version and hash $doc_version_hash"
if [ -z "$doc_version" ]; then
    echo "----EXITING, unable to get docassemble tag version-----"
    exit
fi
if [ -z "$doc_version_hash" ]; then
    echo "----EXITING, unable to get docassemble commit hash-----"
    exit
fi
git checkout $doc_version_hash -B upstream-latest
git checkout $current_branch
echo "Branch 'upstream-latest' is now up to date"
