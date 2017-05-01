# -*- coding: utf-8 -*-
import json
import os

from build_fail import BuildFail
from build_pass import BuildPass
from slackclient import SlackClient


def pipeline_id():
    run_url = os.environ['WERCKER_RUN_URL']
    # Split the url and get the last item.
    # Make sure to remove the trailing '>'
    return run_url.split('/')[-1].replace('>', '')


channel = "#%s" % (os.environ['WERCKER_SLACK_NOTIFY_CHANNEL'])
project_name = os.environ['WERCKER_GIT_REPOSITORY']
branch = os.environ['WERCKER_GIT_BRANCH']
icon_url = os.environ['WERCKER_SLACK_NOTIFY_ICON']

result = os.environ['WERCKER_RESULT']

if not channel:
    channel = '#general'

if result == 'failed':
    # TODO : Elliot -> Get an actual url to where the reports.zip is stored.
    report_url = 'https://i.imgur.com/s85Xa.png'

    message = BuildFail(project_name,
                        pipeline_id(),
                        branch,
                        report_url,
                        icon_url,
                        channel)
else:
    message = BuildPass(project_name,
                        branch,
                        icon_url,
                        os.environ['VERSION_NAME'],
                        channel)

message.send(SlackClient(os.environ['SLACK_BOT_TOKEN']))
