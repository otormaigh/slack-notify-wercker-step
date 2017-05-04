# -*- coding: utf-8 -*-
import json
import os

from build_fail import BuildFail
from build_pass import BuildPass
from slackclient import SlackClient


"""
Split a comma seperated string into a list, removing any white space while your there.
"""
def spliterator(bad_string):
    if bad_string:
        return bad_string.replace(' ', '').split(',')


result = os.environ['WERCKER_RESULT']

"""
Only proceed if we have a vaild build result.
"""
if result:
    icon_url = os.getenv('WERCKER_SLACK_NOTIFY_ICON')
    notify_fail = os.getenv('WERCKER_SLACK_NOTIFY_NOTIFY_ON_FAIL')
    notify_success = os.getenv('WERCKER_SLACK_NOTIFY_NOTIFY_ON_SUCCESS')

    project_name = os.environ['WERCKER_GIT_REPOSITORY']
    branch = os.environ['WERCKER_GIT_BRANCH']

    """
    Check the outcome of the build and send the relevant message.
    """
    slack_client = SlackClient(os.environ['SLACK_BOT_TOKEN'])
    if result == 'failed':
        message = BuildFail(project_name,
                            branch,
                            icon_url)
        if not notify_fail:
            for channel in spliterator(notify_fail):
                message.send(slack_client, channel)
    else:
        message = BuildPass(project_name,
                            icon_url,
                            os.environ['VERSION_NAME'])
        """
        If 'notify_success' is empty set the notify channel to 'default_channel'.
        If its empty too, set the notify channel to '#general'.
        """
        print('notify_success alpha = %s' % notify_success)
        if not notify_success:
            print('notify_success is empty')
            default_channel = os.getenv('WERCKER_SLACK_NOTIFY_DEFAULT_CHANNEL')
            print('default_channel = %s' % default_channel)
            notify_success = default_channel if default_channel else '#general'

        print('notify_success beta = %s' % notify_success)
        for channel in spliterator(notify_success):
            if channel:
                message.send(slack_client, channel)
else:
    print('-----------------------------------------')
    print('No build result found, skipping this step')
    print('-----------------------------------------')
