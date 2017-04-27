#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python
sudo apt-get install -y python-pip

# Install required modules.
sudo pip install requests

python "$WERCKER_STEP_ROOT/notify.py"
