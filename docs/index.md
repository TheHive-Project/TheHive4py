# TheHive4py

TheHive4py is a Python API client for [TheHive](https://thehive-project.org/), a scalable 3-in-1 open source and free security incident response platform designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.

TheHive4py allows analysts to send alerts to TheHive out of different sources. Those alerts can then be previewed and imported into cases using pre-defined templates.

For example, a SOC may ask its constituency to send suspicious email reports to a specific mailbox that a script polls at regular intervals. When a new email is received, the script parses it then calls TheHive4py to create a corresponding alert in TheHive. Once the alert is raised, SOC analysts will get a notification thanks to TheHive's live stream so they can preview it and import it if deemed worth investigating using a specific template.

## Installation

On macOS and Linux, type:
```bash
sudo pip install thehive4py
```

If you are using Python on a Windows operating system, please forgo the `sudo` command.