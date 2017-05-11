
![](https://thehive-project.org/img/logo.png)


[![Join the chat at https://gitter.im/TheHive-Project/TheHive](https://badges.gitter.im/TheHive-Project/TheHive.svg)](https://gitter.im/TheHive-Project/TheHive?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


# TheHive4py
TheHive4py is a Python API client for [TheHive](https://thehive-project.org/), a scalable 3-in-1 open source and free security incident response platform designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.

TheHive4py allows analysts to create cases out of different sources such as email. For example, a SOC may ask its constituency to send suspicious email reports to a specific mailbox that a script polls at regular intervals. When a new email is received, the script parses it then calls TheHive4py to create a corresponding case in TheHive. Once the case has been created, SOC analysts will get a notification thanks to TheHive's Flow so they can start investigating the new case.

# Caution - WIP
TheHive4py is a work in progress. It is considered *beta* software though we are using it on a regular basis for the use case outlined above. The client doesn't leverage yet the richness of TheHive's REST API (which is [partially documented](https://github.com/CERT-BDF/TheHive/wiki/API%20documentation)) but it should be sufficient in most situations. If not, please feel free to contribute and submit pull requests or [request missing features](https://github.com/CERT-BDF/TheHive4py/issues/new) if you are not comfortable with Python.

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
