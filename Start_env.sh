#!/bin/bash
cd ~/projects/myproject
export FLASK_APP=pybo
export FLASK_DEBUG=true
export APP_CONFIG_FILE=/home/smh/projects/myproject/config/production.py
# activate env.
. ~/venvs/myproject/bin/activate
# flask run --host=0.0.0.0