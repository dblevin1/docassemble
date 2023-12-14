#!/usr/bin/bash

function stopfunc {
    cd $SCRIPT_DIR
    #find . -name "dist" -type d -exec rm -r "{}" \;
    find . -name "*egg-info" -type d -exec rm -r "{}" \;
    exit 0
}

trap stopfunc SIGINT SIGTERM

RED='\033[0;31m'
NC='\033[0m' # No Color

install() {
    echo
    echo "------Installing $(pwd)--------"
    pip install .
    ret=$?
    if [ $ret -ne 0 ]; then
        echo -e "${RED}Exiting pip install failed${NC}"
        exit $ret
    fi
    python setup.py sdist 1>/dev/null
    ret=$?
    if [ $ret -ne 0 ]; then
        echo -e "${RED}Exiting python setup failed${NC}"
        exit $ret
    fi
}
upload() {
    echo "------Uploading $(pwd)--------"
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

pip --version
pip install ./docassemble
cd docassemble
python setup.py sdist 1>/dev/null

cd ../docassemble_base
install
cd ../docassemble_demo
install
cd ../docassemble_webapp
install

echo
echo
echo "----------Done installing starting upload------------"
read -p "Press enter to continue"
cd ../docassemble
upload
cd ../docassemble_base
upload
cd ../docassemble_demo
upload
cd ../docassemble_webapp
upload

exit 0
