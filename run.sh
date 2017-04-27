#!/bin/sh

if [ ! "${WEBHOOK_TOKEN}" ]; then
    fail "No webhook token has been set, skipping this step."
fi

sudo apt-get update -y
sudo apt-get install -y python
sudo apt-get install -y python-pip

# Install required modules.
sudo pip install requests

python "$WERCKER_STEP_ROOT/notify.py"
