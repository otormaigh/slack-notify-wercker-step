### Notes
* Post slack message to either a user or channel. Can be list of users/channels.
* Do this on success and failure.
   * Have flag to turn this on/off
* Add interactive buttons.
  * If release build was success, ask whether to deploy or not.
  * If build fails. Open reports, or retry build.
* Add link to downloadable/viewable builds

## Parameters needed
* Slack web hook tokens
  * Can be environment variable saved in Wercker console
* Username/channel to notify
  * Passed in from wercker.yml
  * Both can be empty, but will post to 'general' channel by default if none found.
