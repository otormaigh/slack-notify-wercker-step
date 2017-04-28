#!/bin/sh

if [ ! "${WEBHOOK_TOKEN}" ]; then
    fail "No webhook token has been set, skipping this step."
fi

if [ $(dpkg-query -W -f='${Status}' python 2>/dev/null | grep -c "ok installed") -eq 0 ]; then
  echo "Python not installed. Doing that now."
  sudo apt-get install -y python;
fi

if [ $(dpkg-query -W -f='${Status}' python-pip 2>/dev/null | grep -c "ok installed") -eq 0 ]; then
  echo "Pip not installed. Doing that now."
  sudo apt-get install -y python;
fi

# Install required python modules.
sudo pip install requests

python "$WERCKER_STEP_ROOT/notify.py"
