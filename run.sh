#!/bin/sh

echo "python version $(python --version) running"

python "$WERCKER_STEP_ROOT/notify.py"
