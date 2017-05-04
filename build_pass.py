# -*- coding: utf-8 -*-
"""
Model class used to create a Slack message relative to a successful build.
"""
import calendar
import datetime
import os


def get_elapsed_time():
    started = int(os.environ['WERCKER_MAIN_PIPELINE_STARTED'])
    now = datetime.datetime.utcnow()
    finished = calendar.timegm(now.utctimetuple())
    elapsed = finished - started
    return hours_minutes(elapsed)


def hours_minutes(seconds):
    m, s = divmod(seconds, 60)
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


class BuildPass(object):
    def __init__(self, project_name, icon_url, version_name):
        self.project_name = project_name
        self.icon_url = icon_url
        self.version_name = version_name


    def send(self, slack_client, channel):
        return slack_client.api_call(
                'chat.postMessage',
                channel = channel,
                icon_url = self.icon_url,
                attachments = [
                    dict(
                		color = '#98FB98',
                		attachment_type = 'default',
                		callback_id = 'build_pass',
                        fields = [
                            dict(
                                title = 'Project',
                                value = self.project_name,
                                short = True
                            ),
                            dict(
                                title = 'Time elapsed',
                                value = get_elapsed_time(),
                                short = True
                            ),
                            dict(
                                title = 'Version',
                                value = self.version_name,
                                short = True
                            ),
                            dict(
                                title = 'Started by',
                                value = os.environ['WERCKER_STARTED_BY'],
                                short = True
                            )
                        ]
                    )
                ]
            )
