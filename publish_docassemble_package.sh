#!/usr/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

install_upload() {
    echo "Installing and Uploading ${pwd}"
    pip install --editable .
    python setup.py sdist
    twine upload --config-file "$config_file_loc" --non-interactive dist/*
    ret=$?
    if [ $ret -ne 0 ]; then
        echo -e "${RED}Exiting twine upload failed${NC}"
        exit $ret
    fi
    rm -r dist *egg-info .eggs 2>/dev/null
}

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd $SCRIPT_DIR

python_env_path=../venv_unix/bin/activate
if [[ ! -f $python_env_path ]]; then
    echo "$python_env_path does not exist"
    exit
fi
source $python_env_path
config_file_loc=~/.pypirc
if [[ ! -f $config_file_loc ]]; then
    echo "$config_file_loc does not exist"
    exit
fi

if [ ! -z "$(git status -s)" ]; then
    echo "----EXITING, uncommitted changes found-----"
    exit
fi

cd docassemble
install_upload
cd ../docassemble_base
install_upload
cd ../docassemble_demo
install_upload
cd ../docassemble_webapp
install_upload

exit 0
