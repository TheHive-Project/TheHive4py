import zipfile
from pathlib import Path
from typing import List

import pytest

from tests.utils import TestConfig
from thehive4py import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.sort import Asc
from thehive4py.types.alert import OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import (
    InputBulkUpdateObservable,
    InputUpdateObservable,
    OutputObservable,
)


class TestObservableEndpoint:
    def test_create_single_in_alert_and_get(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_observable = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "domain",
                "data": "example.com",
                "message": "test observable",
            },
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

    def test_create_multiple_in_alert(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        observable_count = 3
        created_observables = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "domain",
                "data": [f"{i}.example.com" for i in range(observable_count)],
                "message": "test observable",
            },
        )

        fetched_observables = thehive.alert.find_observables(alert_id=test_alert["_id"])

        for created_observable in created_observables:
            assert created_observable in fetched_observables

    def test_create_in_alert_from_file_and_download_as_zip(
        self, thehive: TheHiveApi, test_alert: OutputAlert, tmp_path: Path
    ):
        observable_content = "observable content"
        observable_filename = "alert-observable.txt"
        observable_path = str(tmp_path / observable_filename)
        with open(observable_path, "w") as observable_fp:
            observable_fp.write(observable_content)

        created_observable = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "file",
                "message": "file based observable",
            },
            observable_path=observable_path,
        )[0]

        created_attachment = created_observable.get("attachment")
        assert created_attachment

        observable_archive = str(tmp_path / "downloaded-observable.zip")
        thehive.observable.download_attachment(
            observable_id=created_observable["_id"],
            attachment_id=created_attachment["_id"],
            observable_path=observable_archive,
            as_zip=True,
        )

        with zipfile.ZipFile(observable_archive) as archive_fp:
            with archive_fp.open(observable_filename, pwd=b"malware") as downloaded_fp:
                assert downloaded_fp.read().decode() == observable_content

    def test_create_single_in_case_and_get(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        created_observable = thehive.observable.create_in_case(
            case_id=test_case["_id"],
            observable={
                "dataType": "domain",
                "data": "example.com",
                "message": "test observable",
            },
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

    def test_create_multiple_in_case(self, thehive: TheHiveApi, test_case: OutputCase):
        observable_count = 3
        created_observables = thehive.observable.create_in_case(
            case_id=test_case["_id"],
            observable={
                "dataType": "domain",
                "data": [f"{i}.example.com" for i in range(observable_count)],
                "message": "test observable",
            },
        )

        fetched_observables = thehive.case.find_observables(case_id=test_case["_id"])

        for created_observable in created_observables:
            assert created_observable in fetched_observables

    def test_create_in_case_from_file_and_download_as_is(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        observable_content = "observable content"
        observable_filename = "case-observable.txt"
        observable_path = str(tmp_path / observable_filename)
        with open(observable_path, "w") as observable_fp:
            observable_fp.write(observable_content)

        created_observable = thehive.observable.create_in_case(
            case_id=test_case["_id"],
            observable={
                "dataType": "file",
                "message": "file based observable",
            },
            observable_path=observable_path,
        )[0]

        created_attachment = created_observable.get("attachment")
        assert created_attachment

        downloaded_observable_path = str(tmp_path / "downloaded-observable.zip")
        thehive.observable.download_attachment(
            observable_id=created_observable["_id"],
            attachment_id=created_attachment["_id"],
            observable_path=downloaded_observable_path,
            as_zip=False,
        )

        with open(downloaded_observable_path) as downloaded_fp:
            assert downloaded_fp.read() == observable_content

    def test_delete(self, thehive: TheHiveApi, test_observable: OutputObservable):
        observable_id = test_observable["_id"]
        thehive.observable.delete(observable_id=observable_id)
        with pytest.raises(TheHiveError):
            thehive.observable.get(observable_id=observable_id)

    def test_update(self, thehive: TheHiveApi, test_observable: OutputObservable):
        observable_id = test_observable["_id"]
        update_fields: InputUpdateObservable = {
            "dataType": "fqdn",
            "message": "updated observable",
        }
        thehive.observable.update(
            observable_id=test_observable["_id"], fields=update_fields
        )
        updated_observable = thehive.observable.get(observable_id=observable_id)

        for key, value in update_fields.items():
            assert updated_observable.get(key) == value

    def test_bulk_update(
        self, thehive: TheHiveApi, test_observables: List[OutputObservable]
    ):
        observable_ids = [observable["_id"] for observable in test_observables]
        update_fields: InputBulkUpdateObservable = {
            "ids": observable_ids,
            "dataType": "other",
            "message": "updated observable",
        }

        thehive.observable.bulk_update(fields=update_fields)
        updated_observables = thehive.observable.find()

        expected_fields = {
            key: value for key, value in update_fields.items() if key != "ids"
        }
        for updated_task in updated_observables:
            for key, value in expected_fields.items():
                assert updated_task.get(key) == value

    def test_share_and_unshare(
        self,
        thehive: TheHiveApi,
        test_observable: OutputObservable,
        test_config: TestConfig,
    ):
        thehive.observable.share(
            observable_id=test_observable["_id"], organisations=[test_config.main_org]
        )

        # TODO: test `unshare` once a second organisation is allowed by the license
        # thehive.observable.unshare(
        #     observable_id=test_observable["_id"], organisations=[test_config.main_org]
        # )

        # TODO: test `list_shares` better once a second organisation is
        # allowed by the license

        assert (
            len(thehive.observable.list_shares(observable_id=test_observable["_id"]))
            == 0
        )

    def test_find_and_count(
        self, thehive: TheHiveApi, test_observables: List[OutputObservable]
    ):
        found_observables = thehive.observable.find(
            sortby=Asc("_createdAt"),
        )
        observable_count = thehive.observable.count()

        assert found_observables == test_observables
        assert len(test_observables) == observable_count
