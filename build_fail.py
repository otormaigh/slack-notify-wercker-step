# -*- coding : utf-8 -*-
"""
Model class used to create a Slack message relative to a failed build.
"""


class BuildFail(object):
    def __init__(self, project_name, pipeline_id, branch, report_url, icon_url, channel_id = None, ):
        self.project_name = project_name
        self.pipeline_id = pipeline_id
        self.branch = branch
        self.report_url = report_url
        self.icon_url = icon_url
        self.channel_id = channel_id


    def send(self, slack_client):
        slack_client.api_call(
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
                            title = "Branch",
                            value = self.branch,
                            short = True
                        ),
                        dict(
                            title = "Pipeline ID",
                            value = self.pipeline_id,
                            short = True
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
                            text = 'Report',
                            type = 'button',
                            value = self.report_url
                        )
                    ]
                )
            ]
        )
