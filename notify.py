# -*- coding: utf-8 -*-  # noqa
import json
import os
import requests

webhook_token = os.environ['WEBHOOK_TOKEN']
webhook_url = "https://hooks.slack.com/services/%s" % (webhook_token)

#user = os.environ['user']
#channel = os.environ['channel']

#if not user:
#if not channel:
    #channel = '#general'

print("BUILD MESSAGE")
branch = os.environ['WERCKER_GIT_BRANCH']
result = os.environ['WERCKER_RESULT']
build_url = os.environ['WERCKER_RUN_URL']

if result == 'failed':
    color = "#900"
else:
    color = '#36a64f'

message = {
    "channel": '@elliot',
    "text": "%s build %s" % (os.environ['WERCKER_GIT_REPOSITORY'], result),
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
                    "value": build_url,
                    "short": True
                },
                {
                    "title": "Started by",
                    "value": os.environ['WERCKER_STARTED_BY']
                }
            ]
        },
    ]
}
requests.post(webhook_url, json=message)
