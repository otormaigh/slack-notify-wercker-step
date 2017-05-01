# -*- coding: utf-8 -*-
import json
import os
import calendar
import datetime

from build_fail import BuildFail
from build_pass import BuildPass


def pipeline_id():
    run_url = os.environ['WERCKER_RUN_URL']
    # Split the url and get the last item.
    # Make sure to remove the trailing '>'
    return run_url.split('/')[-1].replace('>', '')


user = "@%s" % (os.environ['WERCKER_SLACK_NOTIFY_USER'])
project_name = os.environ['WERCKER_GIT_REPOSITORY']
branch = os.environ['WERCKER_GIT_BRANCH']
icon_url = os.environ['WERCKER_SLACK_NOTIFY_ICON']

result = os.environ['WERCKER_RESULT']

if result == 'failed':
    # TODO : Elliot -> Get an actual url to where the reports.zip is stored.
    report_url = 'https://i.imgur.com/s85Xa.png'

    message = BuildFail(project_name,
                        pipeline_id(),
                        branch,
                        report_url,
                        icon_url,
                        user,)
else:
    message = BuildPass(project_name,
                        branch,
                        icon_url,
                        os.environ['VERSION_NAME'],
                        user,)

message.send("https://hooks.slack.com/services/%s" % os.environ['WEBHOOK_TOKEN'])
