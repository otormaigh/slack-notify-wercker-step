# -*- coding: utf-8 -*-  # noqa
import json
import os
import requests

webhook_token = os.environ['WEBHOOK_TOKEN']
webhook_url = "https://hooks.slack.com/services/%s" % (webhook_token)

author_icon = "%s/%s" % (os.environ['WERCKER_STEP_ROOT'], os.environ['WERCKER_SLACK_NOTIFY_ICON'])
user = "@%s" % (os.environ['WERCKER_SLACK_NOTIFY_USER'])

#channel = "#%s" % (os.environ['channel'])

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
    "channel": user,
    "author_icon": author_icon,
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
                    "title": "Started by",
                    "value": os.environ['WERCKER_STARTED_BY']
                },
                {
                    "title": "URL",
                    "value": build_url,
                    "short": False
                }
            ]
        },
    ]
}
requests.post(webhook_url, json=message)
