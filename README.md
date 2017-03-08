
![](images/thehive-logo.png)
# TheHive4py
TheHive4py is a Python API client for [TheHive](https://thehive-project.org/), a scalable 3-in-1 open source and free security incident response platform designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.

TheHive4py allows analysts to create cases out of different sources such as email. For example, the SOC may ask its constituency to send suspicious email reports to a specific mailbox that a script may poll at regular intervals. When a new email is received, the script will parse it then call TheHive4py to create the case in TheHive. Analysts will be informed that a new case has been created through TheHive's Flow and start their investigation right away.

# Caution - WIP
TheHive4py is a work-in-progress. TheHive authors use it on a regular basis and features will be added as the need arise.

Please note that a new version of TheHive will be released by the end of April / beginning of May 2017 and it will feature a Scala connector framework to handle alerts, which translate to cases if analysts deem them worth investigating, in a more generic and resilient fashion. The connector framework will allow SOCs and CERTs to interface TheHive with SIEMs, email and other services.

When the connector framework is published, TheHive authors may not maintain TheHive4py on the long run but since it is a FOSS, the community can fork it and enhance it the way they see fit. Pull requests will be reviewed by TheHive core team and accepted if they are OK.

# Use It
On macOS and Linux, type:
```
sudo pip install thehive4py
```

If you are using Python on a Windows operating system, please forgo the `sudo` command.

# License
TheHive4py is an open source and free software released under the [AGPL](https://github.com/CERT-BDF/TheHive/blob/master/LICENSE) (Affero General Public License). We, TheHive Project, are committed to ensure that TheHive4py will remain a free and open source project on the long-run.

# Updates
Information, news and updates are regularly posted on [TheHive Project Twitter account](https://twitter.com/thehive_project) and on [the blog](https://blog.thehive-project.org/).

# Contributing
We welcome your contributions. Please feel free to fork the code, play with it, make some patches and send us pull requests.

# Support
Please [open an issue on GitHub](https://github.com/CERT-BDF/TheHive4py/issues/new) if you'd like to report a bug or request a feature.

If you need to contact the project team, send an email to <support@thehive-project.org>.

# Community Discussions
We have set up a Google forum at <https://groups.google.com/a/thehive-project.org/d/forum/users>. To request access, you need a Google account. You may create one [using a Gmail address](https://accounts.google.com/SignUp?hl=en) or [without one](https://accounts.google.com/SignUpWithoutGmail?hl=en).

# Website
<https://thehive-project.org/>
