#!/bin/sh

if [ ! "${WEBHOOK_TOKEN}" ]; then
    fail "No webhook token has been set, skipping this step."
fi

# Install required python modules.
sudo pip install requests

python "$WERCKER_STEP_ROOT/notify.py"
