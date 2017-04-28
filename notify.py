# -*- coding: utf-8 -*-  # noqa
import json
import os
import requests
import calendar
import datetime

def get_elapsed_time():
    started = int(os.environ['WERCKER_MAIN_PIPELINE_STARTED'])
    now = datetime.datetime.utcnow()
    finished = calendar.timegm(now.utctimetuple())
    elapsed = finished - started
    return hours_minutes(elapsed)

def hours_minutes(seconds):
    m, s = divmod(seconds, 60)
    # parts = []
    mins = pluralize(m, 'minute')
    secs = pluralize(s, 'second')
    if mins:
        return mins + ' ' + secs
    return secs

def pluralize(number, word):
    if number:
        phrase = '%s %s' % (number, word)
        if number != 1:
            phrase += 's'
        return phrase
    return ''

webhook_token = os.environ['WEBHOOK_TOKEN']
webhook_url = "https://hooks.slack.com/services/%s" % (webhook_token)

print("BUILD MESSAGE")
branch = os.environ['WERCKER_GIT_BRANCH']
result = os.environ['WERCKER_RESULT']
author_icon = os.environ['WERCKER_SLACK_NOTIFY_ICON']
user = "@%s" % (os.environ['WERCKER_SLACK_NOTIFY_USER'])
#channel = "#%s" % (os.environ['channel'])
run_url = os.environ['WERCKER_RUN_URL']
message = os.environ['WERCKER_SLACK_NOTIFY_MESSAGE']
version_name = os.environ['VERSION_NAME']

if not message:
    message = "%s build %s." % (os.environ['WERCKER_GIT_REPOSITORY'], result)

if not user:
    user = "@elliot"
#if not channel:
    #channel = '#general'

if result == 'failed':
    color = "#900"
else:
    color = '#36a64f'

message = {
    "channel": user,
    "author_icon": author_icon,
    "thumb_url": author_icon,
    "text": message,
    "username": "Wercker",
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": color,
            "fields": [
                {
                    "title": "Started by",
                    "value": os.environ['WERCKER_STARTED_BY'],
                    "short": True
                },
                {
                    "title": "Time elapsed",
                    "value": get_elapsed_time(),
                    "short": True
                },
                {
                    "title": "Version",
                    "value": version_name,
                    "short": True
                }
            ]
        }
    ]
}
requests.post(webhook_url, json=message)
