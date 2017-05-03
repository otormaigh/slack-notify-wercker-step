# -*- coding: utf-8 -*-
"""
Model class used to create a Slack message relative to a failed build.
"""
import os


class BuildFail(object):
    def __init__(self, project_name, branch, icon_url):
        self.project_name = project_name
        self.branch = branch
        self.icon_url = icon_url
        # TODO : Elliot -> Get an actual url to where the reports.zip is stored.
        self.report_url = 'https://i.imgur.com/s85Xa.png'


    """
    Split the url and get the last item, which contains the id.
    Make sure to remove the trailing '>'
    """
    def __id_from_url(self, url):
        return url.split('/')[-1].replace('>', '')


    def send(self, slack_client, channel):
        return slack_client.api_call(
                    'chat.postMessage',
                    channel = channel,
                    icon_url = self.icon_url,
                    attachments = [
                        dict(
                			color = '#FF0033',
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
                                )
                            ],
                            actions = [
                                dict(
                                    name = 'rebuild',
                                    text = 'Rebuild',
                                    type = 'button',
                                    value = ('{"run_id": \"%s\", "app_id": \"%s\"}' % (self.__id_from_url(os.environ['WERCKER_RUN_URL']), self.__id_from_url(os.environ['WERCKER_APPLICATION_URL']))),
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
                                    value = self.report_url
                                )
                            ]
                        )
                    ]
                )
