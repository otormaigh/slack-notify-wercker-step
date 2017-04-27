#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python
sudo apt-get install python-pip

# Install required modules.
sudo pip install requests

echo "python version $(python --version) running"

python "$WERCKER_STEP_ROOT/notify.py"
