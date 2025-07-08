from pathlib import Path
from typing import List

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.helpers import now_to_ts
from thehive4py.query.filters import Eq
from thehive4py.query.sort import Asc
from thehive4py.types.alert import InputBulkUpdateAlert, InputUpdateAlert, OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import InputObservable


class TestAlertEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi):
        created_alert = thehive.alert.create(
            {
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "first",
                "externalLink": "http://",
                "date": 123,
                "tags": ["whatever"],
            }
        )

        fetched_alert = thehive.alert.get(created_alert["_id"])
        assert created_alert == fetched_alert

    def test_update(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]
        update_fields: InputUpdateAlert = {
            "title": "my updated alert",
            "description": "my updated description",
        }
        thehive.alert.update(alert_id=alert_id, fields=update_fields)
        updated_alert = thehive.alert.get(alert_id=alert_id)

        assert updated_alert["title"] == update_fields["title"]
        assert updated_alert["description"] == update_fields["description"]

    def test_bulk_update(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        alert_ids = [alert["_id"] for alert in test_alerts]
        update_fields: InputBulkUpdateAlert = {
            "ids": alert_ids,
            "title": "my updated alert #1",
            "description": "my updated description #1",
        }

        thehive.alert.bulk_update(fields=update_fields)
        updated_alerts = thehive.alert.find()

        for updated_alert in updated_alerts:
            assert updated_alert["title"] == update_fields["title"]
            assert updated_alert["description"] == update_fields["description"]

    def test_follow_and_unfollow(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        thehive.alert.unfollow(alert_id=alert_id)
        unfollowed_alert = thehive.alert.get(alert_id=alert_id)
        assert unfollowed_alert["follow"] is False

        thehive.alert.follow(alert_id=alert_id)
        followed_alert = thehive.alert.get(alert_id=alert_id)
        assert followed_alert["follow"] is True

    def test_promote_to_case(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        case_from_alert = thehive.alert.promote_to_case(alert_id=alert_id)
        promoted_alert = thehive.alert.get(alert_id=alert_id)
        assert promoted_alert.get("caseId") == case_from_alert["_id"]

    def test_promote_to_case_with_additional_fields(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        alert_id = test_alert["_id"]

        case_from_alert = thehive.alert.promote_to_case(
            alert_id=alert_id, fields={"title": "promoted title"}
        )
        promoted_alert = thehive.alert.get(alert_id=alert_id)
        assert promoted_alert.get("caseId") == case_from_alert["_id"]
        assert promoted_alert["title"] != case_from_alert["title"]

    def test_merge_into_case(
        self, thehive: TheHiveApi, test_alert: OutputAlert, test_case: OutputCase
    ):
        alert_id = test_alert["_id"]
        case_id = test_case["_id"]

        merged_case = thehive.alert.merge_into_case(alert_id=alert_id, case_id=case_id)

        merged_alert = thehive.alert.get(alert_id=alert_id)
        assert merged_alert.get("caseId") == merged_case["_id"]

    def test_import_into_case(
        self, thehive: TheHiveApi, test_alert: OutputAlert, test_case: OutputCase
    ):
        alert_id = test_alert["_id"]
        case_id = test_case["_id"]

        imported_case = thehive.alert.import_into_case(
            alert_id=alert_id, case_id=case_id
        )
        imported_alert = thehive.alert.get(alert_id=alert_id)

        assert imported_alert.get("caseId") == imported_case["_id"]

    def test_bulk_merge_into_case(
        self, thehive: TheHiveApi, test_alerts: List[OutputAlert], test_case: OutputCase
    ):
        alert_ids = [alert["_id"] for alert in test_alerts]
        case_id = test_case["_id"]

        merged_case = thehive.alert.bulk_merge_into_case(
            case_id=case_id, alert_ids=alert_ids
        )

        for alert in thehive.alert.find():
            assert alert.get("caseId") == merged_case["_id"]

    def test_find_and_count(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        found_alerts = thehive.alert.find(
            filters=Eq("title", test_alerts[0]["title"])
            | Eq("title", test_alerts[1]["title"]),
            sortby=Asc("_createdAt"),
        )
        alert_count = thehive.alert.count()

        assert found_alerts == test_alerts
        assert len(found_alerts) == alert_count

    def test_delete(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]
        thehive.alert.delete(alert_id)
        with pytest.raises(TheHiveError):
            thehive.alert.get(alert_id)

    def test_bulk_delete(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        alert_ids = [alert["_id"] for alert in test_alerts]
        thehive.alert.bulk_delete(ids=alert_ids)
        for alert_id in alert_ids:
            with pytest.raises(TheHiveError):
                thehive.alert.get(alert_id)

    def test_get_similar_observables(
        self, thehive: TheHiveApi, test_alerts: List[OutputAlert]
    ):
        similar_observables = thehive.alert.get_similar_observables(
            alert_id=test_alerts[0]["_id"], alert_or_case_id=test_alerts[1]["_id"]
        )

        assert similar_observables == []

    def test_create_and_get_observable(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_observables = thehive.alert.create_observable(
            test_alert["_id"], {"dataType": "domain", "data": "example.com"}
        )
        alert_observables = thehive.alert.find_observables(test_alert["_id"])
        assert created_observables == alert_observables

    def test_create_observable_from_file(
        self, thehive: TheHiveApi, test_alert: OutputAlert, tmp_path: Path
    ):
        observable_path = str(tmp_path / "alert-observable.txt")
        with open(observable_path, "w") as observable_fp:
            observable_fp.write("observable content")

        created_observable = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "file",
                "message": "file based observable",
            },
            observable_path=observable_path,
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

        attachment = fetched_observable.get("attachment")
        assert attachment and attachment["name"] in observable_path

    def test_create_alert_with_observables(self, thehive: TheHiveApi):
        created_alert = thehive.alert.create(
            {
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "second",
                "externalLink": "http://",
                "date": 123,
                "tags": ["whatever"],
                "observables": [
                    {"dataType": "url", "data": "example.org"},
                    {"dataType": "mail", "data": "foo@example.org"},
                ],
            }
        )

        fetched_alert = thehive.alert.get(created_alert["_id"])
        # TODO: for some reason alert creation doesn't return _updatedAt and _updatedBy
        # ask backend team  what's the matter
        fetched_alert.pop("_updatedAt")
        fetched_alert.pop("_updatedBy")
        assert created_alert == fetched_alert
        assert created_alert["observableCount"] == 2

    def test_create_alert_with_observable_file(
        self, thehive: TheHiveApi, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "alert-observable.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("observable content")

        alert_observables: List[InputObservable] = [
            {"dataType": "url", "data": "example.com"},
            {"dataType": "file", "attachment": "obs1"},
        ]
        created_alert = thehive.alert.create(
            alert={
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "third",
                "date": 123,
                "observables": alert_observables,
            },
            attachment_map={"obs1": attachment_path},
        )
        assert created_alert["observableCount"] == len(alert_observables)

    def test_find_comments(self, thehive: TheHiveApi, test_alert: OutputAlert):
        created_comment = thehive.comment.create_in_alert(
            alert_id=test_alert["_id"],
            comment={"message": "my first comment"},
        )

        alert_comments = thehive.alert.find_comments(alert_id=test_alert["_id"])

        assert [created_comment] == alert_comments

    def test_create_and_find_procedure(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_procedure = thehive.alert.create_procedure(
            alert_id=test_alert["_id"],
            procedure={
                "occurDate": now_to_ts(),
                "patternId": "T1059.006",
                "tactic": "execution",
                "description": "...",
            },
        )
        alert_procedures = thehive.alert.find_procedures(alert_id=test_alert["_id"])
        assert [created_procedure] == alert_procedures

    def test_add_and_download_attachment(
        self, thehive: TheHiveApi, test_alert: OutputAlert, tmp_path: Path
    ):
        attachment_paths = [str(tmp_path / f"attachment-{i}.txt") for i in range(2)]
        download_attachment_paths = [
            str(tmp_path / f"dl-attachment-{i}.txt") for i in range(2)
        ]

        for path in attachment_paths:
            with open(path, "w") as attachment_fp:
                attachment_fp.write(f"content of {path}")

        added_attachments = thehive.alert.add_attachment(
            alert_id=test_alert["_id"], attachment_paths=attachment_paths
        )

        for attachment, path in zip(added_attachments, download_attachment_paths):
            with pytest.deprecated_call():
                thehive.alert.download_attachment(
                    alert_id=test_alert["_id"],
                    attachment_id=attachment["_id"],
                    attachment_path=path,
                )

        for original, downloaded in zip(attachment_paths, download_attachment_paths):
            with open(original) as original_fp, open(downloaded) as downloaded_fp:
                assert original_fp.read() == downloaded_fp.read()

    def test_add_and_delete_attachment(
        self, thehive: TheHiveApi, test_alert: OutputAlert, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "my-attachment.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("some content...")

        added_attachments = thehive.alert.add_attachment(
            alert_id=test_alert["_id"], attachment_paths=[attachment_path]
        )

        for attachment in added_attachments:
            thehive.alert.delete_attachment(
                alert_id=test_alert["_id"], attachment_id=attachment["_id"]
            )

        assert thehive.alert.find_attachments(alert_id=test_alert["_id"]) == []
