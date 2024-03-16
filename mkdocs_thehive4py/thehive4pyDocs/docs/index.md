# TheHive4py

TheHive4py is a Python API client for [TheHive](https://thehive-project.org/), a scalable 3-in-1 open source and free security incident response platform designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.

TheHive4py allows analysts to send alerts to TheHive out of different sources. Those alerts can then be previewed and imported into cases using pre-defined templates.

For example, a SOC may ask its constituency to send suspicious email reports to a specific mailbox that a script polls at regular intervals. When a new email is received, the script parses it then calls TheHive4py to create a corresponding alert in TheHive. Once the alert is raised, SOC analysts will get a notification thanks to TheHive's live stream so they can preview it and import it if deemed worth investigating using a specific template.

## Features

TheHive4py allows the following features:


=== "Alerts"
    - [X] [Create alert](reference/endpoints/AlertEndpoint/#createself-alert-attachment_map)
    - [X] [Get an alert](reference/endpoints/AlertEndpoint/#getself-alert_id)
    - [X] [Update an alert](reference/endpoints/AlertEndpoint/#updateself-alert_id-fields)
    - [X] [Delete an alert](reference/endpoints/AlertEndpoint/#deleteself-alert_id)
    - [X] [Bulk update alerts](reference/endpoints/AlertEndpoint/#bulk_deleteself-ids)
    - [X] [Bulk delete alerts](reference/endpoints/AlertEndpoint/#promote_to_caseself-alert_id-fields)
    - [X] [Follow an alert](reference/endpoints/AlertEndpoint/#followself-alert_id)
    - [X] [Unfollow an alert](reference/endpoints/AlertEndpoint/#unfollowself-alert_id)
    - [X] [Promote an alert to a case](reference/endpoints/AlertEndpoint/#promote_to_caseself-alert_id-fields)
    - [X] [Create an observable](reference/endpoints/AlertEndpoint/#create_observableself-alert_id-observable-observable_path)
    - [X] [Merge an alert into a case](reference/endpoints/AlertEndpoint/#merge_into_caseself-alert-case_id)
    - [X] [Bulk merge alerts into a case](reference/endpoints/AlertEndpoint/#bulk_merge_into_caseself-case_id-alert_ids)
    - [X] [Find alerts](reference/endpoints/AlertEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count alerts](reference/endpoints/AlertEndpoint/#countself-filters)
    - [X] [Find observables](reference/endpoints/AlertEndpoint/#find_observablesself-alert_id-filters-sortby-paginate)
    - [X] [Find comments](reference/endpoints/AlertEndpoint/#find_commentsself-alert_id-filters-sortby-paginate)
    - [X] [Create procedure](reference/endpoints/AlertEndpoint/#create_procedureself-alert_id-procedure)
    - [X] [Find procedure](reference/endpoints/AlertEndpoint/#find_procedureself-alert_id-filters-sortby-paginate)

=== "Cases"
    - [X] [Create a case](reference/endpoints/CaseEndpoint/#createself-case)
    - [X] [Get a case](reference/endpoints/CaseEndpoint/#getself-case_id)
    - [X] [Delete a case](reference/endpoints/CaseEndpoint/#deleteself-case_id)
    - [X] [Update a case](reference/endpoints/CaseEndpoint/#updateself-case_id-case)
    - [X] [Bulk update cases](reference/endpoints/CaseEndpoint/#bulk_updateselffields)
    - [X] [Merge cases](reference/endpoints/CaseEndpoint/#mergeself-case_ids)
    - [X] [Unlink case](reference/endpoints/CaseEndpoint/#unlink_alertself-case_id-alert_id)
    - [X] [Merge similar observables](reference/endpoints/CaseEndpoint/#merge_similar_observablesself-case_id)
    - [X] [Get linked cases](reference/endpoints/CaseEndpoint/#get_linked_casesself-case_id)
    - [X] [Delete custom field](reference/endpoints/CaseEndpoint/#delete_custom_fieldself-custom_field_id)
    - [X] [Import a case from a file](reference/endpoints/CaseEndpoint/#import_from_fileself-import_case-import_path)
    - [X] [Export a case to a file](reference/endpoints/CaseEndpoint/#export_to_fileself-case_id-password-export_path)
    - [X] [Get the timeline](reference/endpoints/CaseEndpoint/#get_timelineself-case_id)
    - [X] [Add attachment](reference/endpoints/CaseEndpoint/#add_attachmentself-case_id-attachment_paths)
    - [X] [Download attachment](reference/endpoints/CaseEndpoint/#download_attachmentself-case_id-attachment_id-attachment_paths)
    - [X] [Delete attachment](reference/endpoints/CaseEndpoint/#delete_attachmentself-case_id-attachment_id)
    - [X] [List the shares](reference/endpoints/CaseEndpoint/#list_sharesself-case_id)
    - [X] [Share a case](reference/endpoints/CaseEndpoint/#shareself-case_id-shares)
    - [X] [Unshare a case](reference/endpoints/CaseEndpoint/#unshareself-case_id-organisation_ids)
    - [X] [Set a share](reference/endpoints/CaseEndpoint/#set_shareself-case_id-shares)
    - [X] [Remove a share](reference/endpoints/CaseEndpoint/#remove_shareself-share_id)
    - [X] [Update a share](reference/endpoints/CaseEndpoint/#update_shareself-share_id-profile)
    - [X] [Find case](reference/endpoints/CaseEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count cases](reference/endpoints/CaseEndpoint/#countself-filters)
    - [X] [Create a task](reference/endpoints/CaseEndpoint/#create_taskself-case_id-task)
    - [X] [Fins tasks](reference/endpoints/CaseEndpoint/#find_tasksself-case_id-filters-sortby-paginate)
    - [X] [Create observable](reference/endpoints/CaseEndpoint/#create_observableself-case_id-observable-observable_path)
    - [X] [Find observables](reference/endpoints/CaseEndpoint/#find_observablesself-case_id-filters-sortby-paginate)
    - [X] [Create a procedure](reference/endpoints/CaseEndpoint/#create_procedureself-case_id-procedure)
    - [X] [Find procedures](reference/endpoints/CaseEndpoint/#find_proceduresself-case_id-filters-sortby-paginate)
    - [X] [Find attachments](reference/endpoints/CaseEndpoint/#find_attachmentsself-case_id-filters-sortby-paginate)
    - [X] [Find comments](reference/endpoints/CaseEndpoint/#find_commentsself-case_id-filters-sortby-paginate)
    - [X] [Close a case](reference/endpoints/CaseEndpoint/#closeself-case_id-status-summary-impact_status)
    - [X] [Open a case](reference/endpoints/CaseEndpoint/#openself-case_id-status-summary-impact_status)

=== "Comments"
    - [X] [Create in alert](reference/endpoints/CommentEndpoint/#create_in_alertself-alert_id-comment)
    - [X] [Create in case](reference/endpoints/CommentEndpoint/#create_in_caseself-case_id-comment)
    - [X] [Get a comment](reference/endpoints/CommentEndpoint/#getself-comment_id)
    - [X] [Delete a comment](reference/endpoints/CommentEndpoint/#deleteself-comment_id)
    - [X] [Update a comment](reference/endpoints/CommentEndpoint/#updateself-comment_id-fields)

=== "Custom field"
    - [X] [Create a custom field](reference/endpoints/CustomFieldEndpoint/#createself-custom_field)
    - [X] [List custom fields](reference/endpoints/CustomFieldEndpoint/#listself)
    - [X] [Delete a custom field](reference/endpoints/CustomFieldEndpoint/#deleteself-custom_field_id)
    - [X] [Update a custom field](reference/endpoints/CustomFieldEndpoint/#updateself-custom_field_id-fields)

=== "Observable"
    - [X] [Create in alert](reference/endpoints/ObservableEndpoint/#create_in_alertself-alert_id-observable-observable_path)
    - [X] [Create in case](reference/endpoints/ObservableEndpoint/#create_in_caseself-case_id-observable-observable_path)
    - [X] [Get observable](reference/endpoints/ObservableEndpoint/#getself-observable_id)
    - [X] [Delete observable](reference/endpoints/ObservableEndpoint/#deleteself-observable_id)
    - [X] [Update an observable](reference/endpoints/ObservableEndpoint/#updateself-observable_id-fields)
    - [X] [Bulk update](reference/endpoints/ObservableEndpoint/#bulk_updateself-fields)
    - [X] [Share observable](reference/endpoints/ObservableEndpoint/#shareself-observable_id-organisations)
    - [X] [Unshare observable](reference/endpoints/ObservableEndpoint/#unshareself-observable_id-organisations)
    - [X] [List observables](reference/endpoints/ObservableEndpoint/#list_sharesself-observable_id)
    - [X] [Find observable](reference/endpoints/ObservableEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count observables](reference/endpoints/ObservableEndpoint/#countself-filters)
    - [X] [Download atachment](reference/endpoints/ObservableEndpoint/#download_attachmentself-observable_id-attachment_id-observable_path-as_zip)

=== "Observable type"
    - [X] [Create an observable type](reference/endpoints/ObservableTypeEndpoint/#createself-observable_type)
    - [X] [Get an observable type](reference/endpoints/ObservableTypeEndpoint/#getself-observable_type_id)
    - [X] [Delete an observable type](reference/endpoints/ObservableTypeEndpoint/#deleteself-observable_type_id)
    - [X] [Find an observable type](reference/endpoints/ObservableTypeEndpoint/#findself-filters-sortby-paginate)

=== "Organisation"
    - [X] [Create an organisation](reference/endpoints/OrganisationEndpoint/#createself-organisation)
    - [X] [Get an organisation](reference/endpoints/OrganisationEndpoint/#getself-org_id)
    - [X] [Update an organisation](reference/endpoints/OrganisationEndpoint/#updateself-org_id-fields)
    - [X] [Delete an organisation](reference/endpoints/OrganisationEndpoint/#deleteself-org_id)
    - [X] [Link organisations](reference/endpoints/OrganisationEndpoint/#linkself-org_id-other_org_id-link)
    - [X] [Unlink organisation](reference/endpoints/OrganisationEndpoint/#unlinkself-org_id-other_org_id)
    - [X] [List links](reference/endpoints/OrganisationEndpoint/#list_linksself-org_id)
    - [X] [Bulk link](reference/endpoints/OrganisationEndpoint/#bulk_linkself-org_id-links)
    - [X] [List sharing profiles](reference/endpoints/OrganisationEndpoint/#list_sharing_profilesself)
    - [X] [Find organisation](reference/endpoints/OrganisationEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count organisations](reference/endpoints/OrganisationEndpoint/#countself-filters)

=== "Procedure"
    - [X] [Create a procedure in an alert](reference/endpoints/ProcedureEndpoint/#create_in_alertself-alert_id-procedure)
    - [X] [Create a procedure in a case](reference/endpoints/ProcedureEndpoint/#create_in_caseself-case_id-procedure)
    - [X] [Get a procedure](reference/endpoints/ProcedureEndpoint/#getself-procedure_id)
    - [X] [Delete a procedure](reference/endpoints/ProcedureEndpoint/#deleteself-procedure_id)
    - [X] [Update a procedure](reference/endpoints/ProcedureEndpoint/#updateself-procedure_id-fields)
    - [X] [Find a procedure](reference/endpoints/ProcedureEndpoint/#findself-filters-sortby-paginate)

=== "Profile"
    - [X] [Create a profile](reference/endpoints/ProfileEndpoint/#createself-profile)
    - [X] [Get an existing profile](reference/endpoints/ProfileEndpoint/#getself-profile_id)
    - [X] [Delete a profile](reference/endpoints/ProfileEndpoint/#deleteself-profile_id)
    - [X] [Update a profile](reference/endpoints/ProfileEndpoint/#updateself-profile_id-fields)
    - [X] [Find a profile](reference/endpoints/ProfileEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count profiles](reference/endpoints/ProfileEndpoint/#countself-filters)

=== "Task"
    - [X] [Create a task in a case](reference/endpoints/TaskEndpoint/#createself-case_id-task)
    - [X] [Get a task](reference/endpoints/TaskEndpoint/#getself-task_id)
    - [X] [Delete a task](reference/endpoints/TaskEndpoint/#deleteself-task_id)
    - [X] [Update a task](reference/endpoints/TaskEndpoint/#updateself-task_id-fields)
    - [X] [Bulk update](reference/endpoints/TaskEndpoint/#bulk_updateself-fields)
    - [X] [Get required actions](reference/endpoints/TaskEndpoint/#get_required_actionsself-task_id)
    - [X] [Set as required](reference/endpoints/TaskEndpoint/#set_as_requiredself-task_id-org_id)
    - [X] [Set as done](reference/endpoints/TaskEndpoint/#set_as_doneself-task_id-org_id)
    - [X] [Find task](reference/endpoints/TaskEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count task](reference/endpoints/TaskEndpoint/#countself-filters)
    - [X] [Create log](reference/endpoints/TaskEndpoint/#create_logself-task_id-task_log)
    - [X] [Find log](reference/endpoints/TaskEndpoint/#find_logsself-task_id-filters-sortby-paginate)

=== "Task log"
    - [X] [Create a task log](reference/endpoints/TaskLogEndpoint/#createself-task_id-task_log)
    - [X] [Get an existing log](reference/endpoints/TaskLogEndpoint/#getself-task_log_id)
    - [X] [Delete a log](reference/endpoints/TaskLogEndpoint/#deleteself-task_log_id)
    - [X] [Update a log](reference/endpoints/TaskLogEndpoint/#updateself-task_log_id-fields)
    - [X] [Add attachments](reference/endpoints/TaskLogEndpoint/#add_attachmentsself-task_log_id-attachment_paths)
    - [X] [Delete an attachment](reference/endpoints/TaskLogEndpoint/#delete_attachmentself-task_log_id-attachment_id)

=== "Timeline"
    - [X] [Get a case timeline](reference/endpoints/TimelineEndpoint/#getself-case_id)
    - [X] [Create an event](reference/endpoints/TimelineEndpoint/#create_eventself-case_id-event)
    - [X] [Delete an event](reference/endpoints/TimelineEndpoint/#delete_eventself-event_id)
    - [X] [Update an event](reference/endpoints/TimelineEndpoint/#update_eventself-event_id-fields)

=== "User"
    - [X] [Create user](reference/endpoints/UserEndpoint/#createselfuser)
    - [X] [Get user](reference/endpoints/UserEndpoint/#getself-user_id)
    - [X] [Get current user](reference/endpoints/UserEndpoint/#get_currentself)
    - [X] [Delete user](reference/endpoints/UserEndpoint/#deleteself-user_id-organisation)
    - [X] [Update user](reference/endpoints/UserEndpoint/#updateself-user_id-fields)
    - [X] [Lock user](reference/endpoints/UserEndpoint/#lockself-user_id)
    - [X] [Unlock user](reference/endpoints/UserEndpoint/#unlockself-user_id)
    - [X] [Set organisation](reference/endpoints/UserEndpoint/#set_organisationsself-user_id-organisation)
    - [X] [Set password](reference/endpoints/UserEndpoint/#set_passwordself-user_id-password)
    - [X] [Get api key](reference/endpoints/UserEndpoint/#get_apikeyself-user_id)
    - [X] [Remove api key](reference/endpoints/UserEndpoint/#remove_apikeyself-user_id)
    - [X] [Renew apikey](reference/endpoints/UserEndpoint/#renew_apikeyself-user_id)
    - [X] [Find user](reference/endpoints/UserEndpoint/#findself-filters-sortby-paginate)
    - [X] [Count users](reference/endpoints/UserEndpoint/#countself-filters)


## Installation

On macOS and Linux, type:

```bash
sudo pip install thehive4py
```

or if you already installed it, update it by typing

```bash
sudo pip install -U thehive4py
```

If you are using Python on a Windows operating system, please forgo the `sudo` command.

## License

TheHive4py is an open source and free software released under the [AGPL](https://github.com/TheHive-Project/TheHive/blob/master/LICENSE) (Affero General Public License). We, TheHive Project, are committed to ensure that TheHive4py will remain a free and open source project on the long-run.

## Updates

Information, news and updates are regularly posted on [TheHive Project Twitter account](https://twitter.com/thehive_project) and on [the blog](https://blog.thehive-project.org/).

## Contributing

We welcome your contributions. Please feel free to fork the code, play with it, make some patches and send us pull requests using [issues](https://github.com/TheHive-Project/TheHive4py/issues).

We do have a [Code of conduct](code_of_conduct.md). Make sure to check it out before contributing.

## Support

Please [open an issue on GitHub](https://github.com/TheHive-Project/TheHive4py/issues/new) if you'd like to report a bug or request a feature. We are also available on [Gitter](https://gitter.im/TheHive-Project/TheHive) to help you out.

If you need to contact the project team, send an email to <support@thehive-project.org>.

## Community Discussions

We have set up a Google forum at <https://groups.google.com/a/thehive-project.org/d/forum/users>. To request access, you need a Google account. You may create one [using a Gmail address](https://accounts.google.com/SignUp?hl=en) or [without one](https://accounts.google.com/SignUpWithoutGmail?hl=en).

## Website

[https://thehive-project.org/](https://thehive-project.org)
