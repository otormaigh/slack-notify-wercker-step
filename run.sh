#!/bin/sh

if [ ! "${SLACK_BOT_TOKEN}" ]; then
    fail "No token has been set, skipping this step."
fi

# TODO : Elliot -> make the gradle path more dynamic
# for differenct modules
GRADLE_PATH=app/build.gradle                                              # path to the gradle file
GRADLE_FIELD="versionName"                                                # field name
VERSION_TMP=$(grep $GRADLE_FIELD $GRADLE_PATH | awk '{print $2}')         # get value versionName"0.1.0"
export VERSION_NAME=$(echo $VERSION_TMP | sed -e 's/^"//'  -e 's/"$//')   # remove quotes 0.1.0

if [ ! "$VERSION_NAME" ]; then
  export VERSION_NAME="unknown"
fi

pip install -r requirements.txt
python "$WERCKER_STEP_ROOT/notify.py"
