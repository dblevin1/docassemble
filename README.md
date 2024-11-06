# Fork Features/Changes
#### Repo
* less frequent updates for more stable builds
* 4 bash scripts to manage this repo
* github action to auto build docker image
* added docker-compose with external database

#### Features/changes
* added `[FILEPATH /custom/path]` tag for pdf filling, is like [`[FILE ...]`](https://docassemble.org/docs/documents.html#signature%20docx) but only for pdfs and can use any filepath
* added config option `left align signature for pdf fill: False`
* show new package versions for user installed packages
* change userlist page to only show custom privileges (you can still tell who has what default privilege from the icons)
* added config option `pip urls` (list) to override default package repo when installing/upgrading from pip
  * `pip urls:  - https://username:password@example.com`

#### Low impact changes
* allow docassemble packages to be updated via giturl (shouldn't be used for prod, you have to perform a restart manually)
* enabled reset_user_dict logmessage
* disabled "Unable to locate interview session" message
* added session id to error email
* remove 1 second sleep from background_action task

#### Bugfixes
* fix restart session NoneType error when no session exists
* change checkin to reload page when unable to get session

# Help

See the [docassemble web site] for a description of **docassemble**
and installation instructions.

To get help with using **docassemble**, join the [docassemble Slack
group].

[docassemble web site]: https://docassemble.org
[docassemble Slack group]: https://docassemble.org/docs/support.html
