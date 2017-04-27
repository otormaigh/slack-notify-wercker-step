#!/bin/sh

sudo apt-get update -y
sudo apt-get install -y python2.7
sudo apt-get install -y pip

echo "python version $(python --version) running"
echo "pip version $(pip --version) running"

python notify.py
