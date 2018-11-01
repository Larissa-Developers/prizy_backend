#!/usr/bin/env bash
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

# Go into the app root directory
cd "$SCRIPTPATH/../"

# Activate local virtual environment
. $(pipenv --venv)/bin/activate

# Run migrations
python3 manage.py migrate

# Start server
python3 manage.py runserver  0.0.0.0:8000