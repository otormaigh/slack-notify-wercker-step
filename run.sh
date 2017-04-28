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

# variables
GRADLE_PATH=app/build.gradle                                       # path to the gradle file
GRADLE_FIELD="versionName"                                         # field name
VERSION_TMP=$(grep $GRADLE_FIELD $GRADLE_PATH | awk '{print $2}')  # get value versionName"0.1.0"
version_name=$(echo $VERSION_TMP | sed -e 's/^"//'  -e 's/"$//')   # remove quotes 0.1.0

if [ ! "$version_name" ]; then
  version_name="unknown"
fi

python "$WERCKER_STEP_ROOT/notify.py" $version_name
