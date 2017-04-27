#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python
echo "python version = $(python --version)"

sudo apt-get install -y python-pip
echo "pip version = $(pip --version)"

# Install required modules.
sudo pip install requests

python "$WERCKER_STEP_ROOT/notify.py"
