#!/usr/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

git-resolve-conflict() {
    STRATEGY="$1"
    FILE_PATH="$2"

    if [ -z "$FILE_PATH" ] || [ -z "$STRATEGY" ]; then
        echo "Usage:   git-resolve-conflict <strategy> <file>"
        echo ""
        echo "Example: git-resolve-conflict --ours package.json"
        echo "Example: git-resolve-conflict --union package.json"
        echo "Example: git-resolve-conflict --theirs package.json"
        return
    fi

    got_status=$(git status -s)
    if [[ $got_status != *"UU $FILE_PATH"* ]]; then
        #echo "Skipping $FILE_PATH, it looks good"
        return
    fi
    echo "Resolving conflict for: $FILE_PATH"

    git show :1:"$FILE_PATH" >./tmp.common
    git show :2:"$FILE_PATH" >./tmp.ours
    git show :3:"$FILE_PATH" >./tmp.theirs

    git merge-file "$STRATEGY" -p ./tmp.ours ./tmp.common ./tmp.theirs >"$FILE_PATH"
    git add "$FILE_PATH"

    rm ./tmp.common
    rm ./tmp.ours
    rm ./tmp.theirs
}

git merge upstream-latest
git-resolve-conflict --theirs .bumpversion.cfg
git-resolve-conflict --theirs docassemble/setup.py
git-resolve-conflict --theirs docassemble_base/setup.py
git-resolve-conflict --theirs docassemble_demo/setup.py
git-resolve-conflict --theirs docassemble_webapp/setup.py
git-resolve-conflict --theirs docassemble/docassemble/__init__.py
git-resolve-conflict --theirs docassemble_base/docassemble/base/__init__.py
git-resolve-conflict --theirs docassemble_demo/docassemble/demo/__init__.py
git-resolve-conflict --theirs docassemble_webapp/docassemble/webapp/__init__.py
git-resolve-conflict --theirs docassemble_webapp/docassemble/webapp/setup.py
git-resolve-conflict --theirs Docker/VERSION
git-resolve-conflict --theirs docassemble_webapp/docassemble/webapp/data/VERSION.txt
git-resolve-conflict --ours CHANGELOG.md
#sed -i '1s;^;Merge ;' .git/SQUASH_MSG
echo "-----Status Remaining------"
git status -s
echo "----------Done-------------"
