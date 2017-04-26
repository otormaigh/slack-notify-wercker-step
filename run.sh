#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python2.7
echo "python version $(python --version) running"

python notify.py
