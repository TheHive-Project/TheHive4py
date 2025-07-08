from pathlib import Path
from typing import List

import pytest

from tests.utils import TestConfig
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.helpers import now_to_ts
from thehive4py.query.filters import Eq
from thehive4py.query.page import Paginate
from thehive4py.query.sort import Asc
from thehive4py.types.alert import OutputAlert
from thehive4py.types.case import (
    CaseStatus,
    ImpactStatus,
    InputBulkUpdateCase,
    InputCaseLink,
    InputUpdateCase,
    InputURLLink,
    OutputCase,
)
from thehive4py.types.case_template import OutputCaseTemplate
from thehive4py.types.observable import InputObservable
from thehive4py.types.page import InputUpdateCasePage, OutputCasePage
from thehive4py.types.share import InputShare


class TestCaseEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi):
        created_case = thehive.case.create(
            case={"title": "my first case", "description": "..."}
        )

        fetched_case = thehive.case.get(created_case["_id"])

        # TODO: sometimes timeToDetect can be different between fetched and created
        # probably it's a backend bug
        fetched_case["timeToDetect"] = created_case["timeToDetect"] = 0
        assert created_case == fetched_case

    def test_update(self, thehive: TheHiveApi, test_case: OutputCase):
        case_id = test_case["_id"]
        update_fields: InputUpdateCase = {
            "title": "my updated case",
            "description": "my updated description",
        }
        thehive.case.update(case_id=case_id, fields=update_fields)
        updated_case = thehive.case.get(case_id=case_id)

        for key, value in update_fields.items():
            assert updated_case.get(key) == value

    def test_update_with_deprecation_warning(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        case_id = test_case["_id"]
        update_fields: InputUpdateCase = {
            "title": "my updated case",
            "description": "my updated description",
        }
        with pytest.deprecated_call():
            thehive.case.update(case_id=case_id, case=update_fields)
        updated_case = thehive.case.get(case_id=case_id)

        for key, value in update_fields.items():
            assert updated_case.get(key) == value

    def test_update_with_wrong_argument_error(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        case_id = test_case["_id"]
        update_fields: InputUpdateCase = {
            "title": "my updated case",
            "description": "my updated description",
        }
        wrong_kwargs = {"case_fields": update_fields, "what": "ever"}
        with pytest.raises(TheHiveError, match=rf".*{list(wrong_kwargs.keys())}.*"):
            thehive.case.update(case_id=case_id, **wrong_kwargs)  # type:ignore

    def test_bulk_update(self, thehive: TheHiveApi, test_cases: List[OutputCase]):
        case_ids = [case["_id"] for case in test_cases]
        update_fields: InputBulkUpdateCase = {
            "ids": case_ids,
            "title": "my updated case",
            "description": "my updated description",
        }

        thehive.case.bulk_update(fields=update_fields)
        updated_cases = thehive.case.find()

        for updated_case in updated_cases:
            assert updated_case["title"] == update_fields["title"]
            assert updated_case["description"] == update_fields["description"]

    def test_merge(self, thehive: TheHiveApi, test_cases: List[OutputCase]):
        case_ids = [case["_id"] for case in test_cases]

        merged_case = thehive.case.merge(case_ids=case_ids)

        assert merged_case["title"] == " / ".join(
            [case["title"] for case in test_cases]
        )

        for case_id in case_ids:
            with pytest.raises(TheHiveError):
                thehive.case.get(case_id)

    def test_unlink_alert(
        self, thehive: TheHiveApi, test_case: OutputCase, test_alert: OutputAlert
    ):
        alert_id = test_alert["_id"]
        case_id = test_case["_id"]

        thehive.alert.merge_into_case(alert_id=alert_id, case_id=case_id)
        linked_alert = thehive.alert.get(alert_id=alert_id)
        assert linked_alert.get("caseId") == case_id

        thehive.case.unlink_alert(case_id=case_id, alert_id=alert_id)
        unlinked_alert = thehive.alert.get(alert_id=alert_id)
        assert unlinked_alert.get("caseId") is None

    def test_merge_similar_observables(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        case_id = test_case["_id"]
        thehive.case.create_observable(
            case_id=case_id, observable={"dataType": "ip", "data": "192.168.0.1"}
        )
        thehive.case.create_observable(
            case_id=case_id, observable={"dataType": "ip", "data": "192.168.0.2"}
        )

        result = thehive.case.merge_similar_observables(case_id=case_id)
        assert result == {"deleted": 0, "untouched": 2, "updated": 0}

    def test_get_linked_cases(self, thehive: TheHiveApi, test_cases: List[OutputCase]):
        common_observable: InputObservable = {
            "data": "example.com",
            "dataType": "domain",
        }

        for case in test_cases:
            thehive.case.get(case_id=case["_id"])
            thehive.case.create_observable(
                case_id=case["_id"], observable=common_observable
            )

        assert test_cases[1]["_id"] in [
            linked_case["_id"]
            for linked_case in thehive.case.get_linked_cases(
                case_id=test_cases[0]["_id"]
            )
        ]

    def test_export_and_import(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        archive_path = str(tmp_path / "export.thar")
        password = "test"
        thehive.case.export_to_file(
            case_id=test_case["_id"], password=password, export_path=archive_path
        )

        import_results = thehive.case.import_from_file(
            import_case={"password": password},
            import_path=archive_path,
        )
        assert import_results["case"]["title"] == test_case["title"]
        assert import_results["case"]["description"] == test_case["description"]

    def test_get_timeline(self, thehive: TheHiveApi, test_case: OutputCase):
        timeline = thehive.case.get_timeline(case_id=test_case["_id"])
        assert timeline["events"]

    def test_apply_case_template(
        self,
        thehive: TheHiveApi,
        test_case: OutputCase,
        test_case_template: OutputCaseTemplate,
    ):
        assert (
            set(test_case_template.get("tags", [])).issubset(
                set(test_case.get("tags", []))
            )
            is False
        )

        thehive.case.apply_case_template(
            fields={
                "ids": [test_case["_id"]],
                "caseTemplate": test_case_template["name"],
                "updateTags": True,
            }
        )

        updated_case = thehive.case.get(case_id=test_case["_id"])

        assert (
            set(test_case_template.get("tags", [])).issubset(
                set(updated_case.get("tags", []))
            )
            is True
        )

    def test_change_owner_organisation(
        self, thehive: TheHiveApi, test_case: OutputCase, test_config: TestConfig
    ):
        thehive.case.change_owner_organisation(
            case_id=test_case["_id"], fields={"organisation": test_config.main_org}
        )

    def test_manage_access(self, thehive: TheHiveApi, test_case: OutputCase):
        assert test_case["access"]["_kind"] == "OrganisationAccessKind"
        thehive.case.manage_access(
            case_id=test_case["_id"],
            fields={
                "access": {"_kind": "UserAccessKind", "users": ["admin@thehive.local"]}
            },
        )
        restricted_case = thehive.case.get(case_id=test_case["_id"])
        assert restricted_case["access"]["_kind"] == "UserAccessKind"

    def test_get_similar_observables(
        self, thehive: TheHiveApi, test_cases: List[OutputCase]
    ):
        similar_observables = thehive.case.get_similar_observables(
            case_id=test_cases[0]["_id"], alert_or_case_id=test_cases[1]["_id"]
        )

        assert similar_observables == []

    def test_link_and_unlink_case_with_case(
        self, thehive: TheHiveApi, test_cases: List[OutputCase]
    ):
        case_link: InputCaseLink = {"type": "whatever", "caseId": test_cases[1]["_id"]}

        thehive.case.link_case(
            case_id=test_cases[0]["_id"],
            fields=case_link,
        )
        linked_case = thehive.case.find(
            filters=Eq("_id", test_cases[0]["_id"]),
            paginate=Paginate(start=0, end=1, extra_data=["links"]),
        )[0]
        assert (
            linked_case["extraData"]["links"]["caseLinks"][0]["caseId"]
            == test_cases[1]["_id"]
        )

        thehive.case.delete_case_link(case_id=test_cases[0]["_id"], fields=case_link)
        unlinked_case = thehive.case.find(
            filters=Eq("_id", test_cases[0]["_id"]),
            paginate=Paginate(start=0, end=1, extra_data=["links"]),
        )[0]
        assert unlinked_case["extraData"]["links"]["caseLinks"] == []

    def test_link_and_unlink_case_with_url(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        external_url = "https://example.com"
        url_link: InputURLLink = {"type": "whatever", "url": external_url}

        thehive.case.link_url(case_id=test_case["_id"], fields=url_link)
        linked_case = thehive.case.find(
            filters=Eq("_id", test_case["_id"]),
            paginate=Paginate(start=0, end=1, extra_data=["links"]),
        )[0]
        assert (
            linked_case["extraData"]["links"]["externalLinks"][0]["url"] == external_url
        )

        thehive.case.delete_url_link(case_id=test_case["_id"], fields=url_link)
        unlinked_case = thehive.case.find(
            filters=Eq("_id", test_case["_id"]),
            paginate=Paginate(start=0, end=1, extra_data=["links"]),
        )[0]
        assert unlinked_case["extraData"]["links"]["externalLinks"] == []

    def test_link_types(self, thehive: TheHiveApi):
        assert thehive.case.get_link_types() == []

    def test_add_and_download_attachment(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        attachment_paths = [str(tmp_path / f"attachment-{i}.txt") for i in range(2)]
        download_attachment_paths = [
            str(tmp_path / f"dl-attachment-{i}.txt") for i in range(2)
        ]

        for path in attachment_paths:
            with open(path, "w") as attachment_fp:
                attachment_fp.write(f"content of {path}")

        added_attachments = thehive.case.add_attachment(
            case_id=test_case["_id"], attachment_paths=attachment_paths
        )

        for attachment, path in zip(added_attachments, download_attachment_paths):
            with pytest.deprecated_call():
                thehive.case.download_attachment(
                    case_id=test_case["_id"],
                    attachment_id=attachment["_id"],
                    attachment_path=path,
                )

        for original, downloaded in zip(attachment_paths, download_attachment_paths):
            with open(original) as original_fp, open(downloaded) as downloaded_fp:
                assert original_fp.read() == downloaded_fp.read()

    def test_add_and_delete_attachment(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "my-attachment.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("some content...")

        added_attachments = thehive.case.add_attachment(
            case_id=test_case["_id"], attachment_paths=[attachment_path]
        )

        for attachment in added_attachments:
            thehive.case.delete_attachment(
                case_id=test_case["_id"], attachment_id=attachment["_id"]
            )

        assert thehive.case.find_attachments(case_id=test_case["_id"]) == []

    @pytest.mark.skip(reason="organisation name is not accepted by unshare")
    def test_share_and_unshare(self, thehive: TheHiveApi, test_case: OutputCase):
        organisation = "share-org"
        share: InputShare = {"organisation": organisation}

        thehive.case.share(case_id=test_case["_id"], shares=[share])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == 1

        thehive.case.unshare(case_id=test_case["_id"], organisation_ids=[organisation])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == 1

    @pytest.mark.skip(reason="integrator container only supports a single org ")
    def test_share_and_remove_share(self, thehive: TheHiveApi, test_case: OutputCase):
        organisation = "share-org"
        share: InputShare = {"organisation": organisation}

        shares = thehive.case.share(case_id=test_case["_id"], shares=[share])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == 1

        thehive.case.remove_share(share_id=shares[0]["_id"])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == 0

    @pytest.mark.skip(reason="integrator container only supports a single org ")
    def test_share_and_set_share(self, thehive: TheHiveApi, test_case: OutputCase):
        organisation = "share-org"
        share: InputShare = {"organisation": organisation}

        shares = thehive.case.share(case_id=test_case["_id"], shares=[share])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == len(shares)

        set_shares = thehive.case.set_share(case_id=test_case["_id"], shares=[])
        assert len(thehive.case.list_shares(case_id=test_case["_id"])) == len(
            set_shares
        )

    def test_find_and_count(self, thehive: TheHiveApi, test_cases: List[OutputCase]):
        filters = Eq("title", test_cases[0]["title"]) | Eq(
            "title", test_cases[1]["title"]
        )
        found_cases = thehive.case.find(
            filters=filters,
            sortby=Asc("_createdAt"),
        )

        case_count = thehive.case.count(filters=filters)

        assert found_cases == test_cases
        assert len(test_cases) == case_count

    def test_delete(self, thehive: TheHiveApi, test_case: OutputCase):
        case_id = test_case["_id"]
        thehive.case.delete(case_id)
        with pytest.raises(TheHiveError):
            thehive.case.get(case_id)

    def test_create_and_get_observable(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        created_observables = thehive.case.create_observable(
            test_case["_id"], {"dataType": "domain", "data": "example.com"}
        )
        case_observables = thehive.case.find_observables(test_case["_id"])
        assert created_observables == case_observables

    def test_create_observable_from_file(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        observable_path = str(tmp_path / "case-observable.txt")
        with open(observable_path, "w") as observable_fp:
            observable_fp.write("observable content")

        created_observable = thehive.observable.create_in_case(
            case_id=test_case["_id"],
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

    def test_create_and_get_task(self, thehive: TheHiveApi, test_case: OutputCase):
        created_task = thehive.case.create_task(
            case_id=test_case["_id"], task={"title": "my task"}
        )
        case_tasks = thehive.case.find_tasks(case_id=test_case["_id"])
        assert created_task in case_tasks

    def test_close_and_open(self, thehive: TheHiveApi, test_case: OutputCase):
        case_id = test_case["_id"]
        assert test_case["status"] == "New"
        close_status = CaseStatus.TruePositive
        close_impact = ImpactStatus.WithImpact
        close_summary = "Closed..."
        thehive.case.close(
            case_id=case_id,
            status=close_status,
            summary=close_summary,
            impact_status=close_impact,
        )
        closed_case = thehive.case.get(case_id)
        assert closed_case["status"] == close_status
        assert closed_case.get("impactStatus") == close_impact
        assert closed_case.get("summary") == close_summary

        open_status = CaseStatus.InProgress
        thehive.case.open(case_id, status=open_status)
        reopened_case = thehive.case.get(case_id)
        assert reopened_case["status"] == open_status

    def test_find_comments(self, thehive: TheHiveApi, test_case: OutputCase):
        created_comment = thehive.comment.create_in_case(
            case_id=test_case["_id"],
            comment={"message": "my first comment"},
        )

        case_comments = thehive.case.find_comments(case_id=test_case["_id"])

        assert [created_comment] == case_comments

    def test_create_and_find_procedure(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        created_procedure = thehive.case.create_procedure(
            case_id=test_case["_id"],
            procedure={
                "occurDate": now_to_ts(),
                "patternId": "T1059.007",
                "tactic": "execution",
                "description": "...",
            },
        )
        case_procedures = thehive.case.find_procedures(case_id=test_case["_id"])
        assert [created_procedure] == case_procedures

    def test_create_and_find_page(self, thehive: TheHiveApi, test_case: OutputCase):
        created_page = thehive.case.create_page(
            case_id=test_case["_id"],
            page={"title": "my case page", "category": "testing", "content": "..."},
        )

        case_pages = thehive.case.find_pages(case_id=test_case["_id"])
        assert [created_page] == case_pages

    def test_update_and_delete_page(
        self, thehive: TheHiveApi, test_case: OutputCase, test_case_page: OutputCasePage
    ):
        update_page: InputUpdateCasePage = {"title": "my updated case page"}
        thehive.case.update_page(
            case_id=test_case["_id"],
            page_id=test_case_page["_id"],
            page=update_page,
        )

        updated_case_page = thehive.case.find_pages(
            case_id=test_case["_id"], filters=Eq("_id", test_case_page["_id"])
        )[0]

        for key, value in update_page.items():
            assert updated_case_page.get(key) == value

        thehive.case.delete_page(
            case_id=test_case["_id"], page_id=test_case_page["_id"]
        )
        assert len(thehive.case.find_pages(case_id=test_case["_id"])) == 0
