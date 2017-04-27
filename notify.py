# -*- coding: utf-8 -*-  # noqa
import json
import os
import requests
import sys

webhook_token = os.environ['WEBHOOK_TOKEN']
webhook_url = "https://hooks.slack.com/services/%s" % (webhook_token)

# channel = os.environ['CHANNEL']
user = os.environ['channel']

print("BUILD MESSAGE")
branch = os.environ['WERCKER_GIT_BRANCH']
result = os.environ['WERCKER_RESULT']
url = os.environ('WERCKER_APPLICATION_URL')

if result == 'failed':
    color = "#900"
else:
    color = '#36a64f'

message = {
    "channel": '@elliot',
    "text": "Build %s" % (result),
    "username": "Wercker",
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": color,
            "fields": [
                {
                    "title": "Branch",
                    "value": branch,
                    "short": True
                },
                {
                    "title": "URL",
                    "value": url,
                    "short": True
                },
                {
                    "title": "Commit",
                    "value": os.environ('WERCKER_GIT_COMMIT')
                }
            ]
        },
    ]
}

print(message)
requests.post(webhook_url, json=message)
