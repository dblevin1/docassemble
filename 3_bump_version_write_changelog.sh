#!/usr/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

commit_changes() {
    echo -e "Will commit with message ${RED}'Bump Version: $VERSION → $NEWVERSION'${NC}"
    read -p "Press enter to continue"
    git add *
    git commit -m "Bump Version: $VERSION → $NEWVERSION"
    git push
    git tag "$NEWVERSION"
    git push --tags
}

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd $SCRIPT_DIR

python_env_path=../venv/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Already in virtual env not activating..."
else
    source $python_env_path
    echo "Activated virtual env"
fi

if [ -z "$2" ]; then
    VERSIONPART="release"
    echo "Setting version part to '$VERSIONPART' out of {major}.{minor}.{patch}.{release}"
else
    VERSIONPART="$2"
fi
if [ ! -z "$(git status -s)" ]; then
    echo "----EXITING, uncommitted changes found-----"
    exit
fi

VERSION=$(cat docassemble/setup.py | grep "version='" | sed "s/.*version='//" | sed "s/',//")
if [ -z "$VERSION" ]; then
    echo "Exiting could not get current docassemble version"
    exit
fi

echo "Bumping version"
bumpversion --no-commit --no-tag $VERSIONPART
ret=$?
if [ $ret -ne 0 ]; then
    echo -e "${RED}Exiting bumpversion failed${NC}"
    exit $ret
fi

git add *
git add .bumpversion.cfg
NEWVERSION=$(cat docassemble/setup.py | grep "version='" | sed "s/.*version='//" | sed "s/',//")
if [ -z "$NEWVERSION" ]; then
    echo -e "${RED}Exiting could not get new docassemble version${NC}"
    exit
fi
echo "New Version:$NEWVERSION"

if [[ -f "./CHANGELOG.md" ]]; then
    echo "Adding info to changelog"
    git-changelog -i -o CHANGELOG.md --bump "$NEWVERSION" -s add,fix,change,remove,merge,doc -n pep440
else
    echo "Creating changelog"
    git-changelog -o CHANGELOG.md --bump "$NEWVERSION" -s add,fix,change,remove,merge,doc -n pep440
fi
ret=$?
if [ $ret -ne 0 ]; then
    echo -e "${RED}Exiting git-changelog failed${NC}"
    exit $ret
fi
git add CHANGELOG.md

commit_changes

exit 0
