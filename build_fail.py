# -*- coding: utf-8 -*-
"""
Model class used to create a Slack message relative to a failed build.
"""
import os
import requests


class BuildFail(object):
    def __init__(self, project_name, branch, report_url, icon_url, channel_id = None, ):
        self.project_name = project_name
        self.branch = branch
        self.report_url = report_url
        self.icon_url = icon_url
        self.channel_id = channel_id


    """
    Split the url and get the last item, which contains the id.
    Make sure to remove the trailing '>'
    """
    def __id_from_url(url):
        return url.split('/')[-1].replace('>', '')


    def send(self, slack_client):
        return slack_client.api_call(
                    'chat.postMessage',
                    channel = self.channel_id,
                    icon_url = self.icon_url,
                    attachments = [
                        dict(
                			color = '#ff0033',
                			attachment_type = 'default',
                			callback_id = 'build_fail',
                            fields = [
                                dict(
                                    title = 'Project',
                                    value = self.project_name,
                                    short = True
                                ),
                                dict(
                                    title = 'Status',
                                    value = 'Failed',
                                    short = True
                                ),
                                dict(
                                    title = 'Branch',
                                    value = self.branch,
                                    short = True
                                ),
                                dict(
                                    title = 'Run ID',
                                    value = self.__id_from_url(os.environ['WERCKER_RUN_URL']),
                                    short = True
                                ),
                                dict(
                                    title = 'App ID',
                                    value = self.__id_from_url(os.environ['WERCKER_APPLICATION_URL'])
                                )
                            ],
                            actions = [
                                dict(
                                    name = 'rebuild',
                                    text = 'Rebuild',
                                    type = 'button',
                                    value = 'rebuild',
                                    style = 'danger',
                                    confirm = dict(
                                        title = 'Are you sure?',
                                        text = ('Are you sure you want to rebuild %s?' % self.project_name),
                                        ok_text = 'Yes',
                                        dismiss_text = 'No'
                                    )
                                ),
                                dict(
                                    name = 'report',
                                    text = 'View report',
                                    type = 'button',
                                    value = ('{"run_id": %s,"app_id": %s}', % (self.__id_from_url(os.environ['WERCKER_RUN_URL']), self.__id_from_url(os.environ['WERCKER_APPLICATION_URL'])))
                                )
                            ]
                        )
                    ]
                )
