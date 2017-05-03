# -*- coding: utf-8 -*-
import json
import os

from build_fail import BuildFail
from build_pass import BuildPass
from slackclient import SlackClient


"""
Split a comma seperated string into a list, removing any white space while your there.s
"""
def spliterator(bad_list):
    return bad_list.replace(' ', '').split(',')


result = os.environ['WERCKER_RESULT']

"""
Only proceed if we have a vaild build result.
"""
if result:
    icon_url = os.getenv('WERCKER_SLACK_NOTIFY_ICON')
    notify_fail = spliterator(os.getenv('WERCKER_SLACK_NOTIFY_NOTIFY_ON_FAIL'))
    notify_success = spliterator(os.getenv('WERCKER_SLACK_NOTIFY_NOTIFY_ON_SUCCESS'))

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
            for channel in notify_fail:
                message.send(slack_client, channel)
    else:
        message = BuildPass(project_name,
                            icon_url,
                            os.environ['VERSION_NAME'])
        """
        If 'notify_success' is empty set the notify channel to 'default_channel'.
        If its empty too, set the notify channel to '#general'.
        """
        if not notify_success:
            default_channel = os.getenv('WERCKER_SLACK_NOTIFY_DEFAULT_CHANNEL')
            if default_channel:
                notify_success = default_channel
            else:
                notify_success = '#general'

        print('notify_success = ', notify_success)
        for channel in notify_success:
            message.send(slack_client, channel)
else:
    print('-----------------------------------------')
    print('No build result found, skipping this step')
    print('-----------------------------------------')
