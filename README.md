Slack notify
============

Post a notification to either a Slack channel or directly to a user or both.

Can be triggered on successful or unsuccessful builds.

### Environment Variables
None of the following variables are required when calling this step, but it is advised to input as much information as possible to best suit your build.
If no `notify_on_success` or `default_channel` is set, upon a successful build a message will be sent to the `#general` channel, if the build fails, not message will be sent.

* default_channel: A single channel to use as the default for all successful builds.

  e.g.
  `default_channel: '#general`
* notify_on_success: Comma separated list of channels and/or users to notify after a successful build has completed. If no values are passed here

  e.g.
  `notify_on_success: '#general,@elliot,#wercker,@project_channel'`
* notify_on_fail: Comma separated list of channels and/or users to notify after a failed build has completed.

  e.g.
  `notify_on_fail: '#shame,@elliot,#nothing_to_see_here'`
* icon_url: A valid url pointing to a icon that will be user as the message icon when posting a message to slack.

  e.g.
  `icon_url: 'https://www.someurl.ie/icon.png'`

### Usage
Add this as a an `after-step` to your build.

```
after-steps:
  - tapadoo/slack-notify:
      channel: '#general, #random, @elliot'
      icon: 'https://apps.tapadoo.com/icons/stc.png'
```

If you want to use a specific version of this step add `@versionName` to the end of the step name. See the [Project detail](https://app.wercker.com/applications/59021e4cd3bae80100206b1f/tab/details/) page for a list of available releases.

```
after-steps:
  - tapadoo/slack-notify@0.1.0:
```
