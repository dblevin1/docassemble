#!/usr/bin/bash

PACKAGE_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")" # This follows the symlink to the docker-compose file
echo "PACKAGE_DIR=$PACKAGE_DIR"
echo "SCRIPT_DIR=$SCRIPT_DIR"
cd $SCRIPT_DIR

docker-compose cp "$PACKAGE_DIR/docassemble_webapp/docassemble/webapp/." docassemble:/usr/share/docassemble/local3.10/lib/python3.10/site-packages/docassemble/webapp/
docker-compose cp "$PACKAGE_DIR/docassemble_base/docassemble/base/." docassemble:/usr/share/docassemble/local3.10/lib/python3.10/site-packages/docassemble/base/
docker-compose exec docassemble chown -R www-data:www-data /usr/share/docassemble/local3.10/lib/python3.10/site-packages/docassemble/webapp/
docker-compose exec docassemble chown -R www-data:www-data /usr/share/docassemble/local3.10/lib/python3.10/site-packages/docassemble/base/
docker-compose exec docassemble supervisorctl start reset
exit
