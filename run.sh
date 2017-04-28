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
  sudo apt-get install -y python-pip;
fi

# Install required python modules.
sudo pip install requests

GRADLE_PATH=gradle.properties                                         # path to the gradle file
GRADLE_FIELD="STABLE_VERSION"                                         # field name

version_name=$(grep $GRADLE_FIELD $GRADLE_PATH | awk '{print $3}')    # get value STABLE_VERSION=0.1.0

if [ ! "$version_name" ]; then
  version_name="unknown"
fi

python "$WERCKER_STEP_ROOT/notify.py" $version_name
