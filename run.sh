#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python

echo "python version $(python --version) running"

python "$WERCKER_STEP_ROOT/notify.py"
