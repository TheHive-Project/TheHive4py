from pathlib import Path

from tests.utils import TestConfig
from thehive4py.client import TheHiveApi
from thehive4py.query.filters import Eq


class TestOrganisationEndpoint:
    def test_add_and_download_attachment_to_main_org(
        self, thehive: TheHiveApi, tmp_path: Path
    ):
        attachment_paths = [str(tmp_path / f"attachment-{i}.txt") for i in range(2)]
        download_attachment_paths = [
            str(tmp_path / f"dl-attachment-{i}.txt") for i in range(2)
        ]

        for path in attachment_paths:
            with open(path, "w") as attachment_fp:
                attachment_fp.write(f"content of {path}")

        added_attachments = thehive.organisation.add_attachment(
            attachment_paths=attachment_paths
        )

        for attachment, path in zip(added_attachments, download_attachment_paths):
            thehive.organisation.download_attachment(
                attachment_id=attachment["_id"],
                attachment_path=path,
            )

        for original, downloaded in zip(attachment_paths, download_attachment_paths):
            with open(original) as original_fp, open(downloaded) as downloaded_fp:
                assert original_fp.read() == downloaded_fp.read()

    def test_add_and_delete_attachment_to_main_org(
        self, thehive: TheHiveApi, tmp_path: Path, test_config: TestConfig
    ):
        attachment_path = str(tmp_path / "my-attachment.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("some content...")

        added_attachments = thehive.organisation.add_attachment(
            attachment_paths=[attachment_path]
        )

        for attachment in added_attachments:
            thehive.organisation.delete_attachment(attachment_id=attachment["_id"])

        assert thehive.organisation.find_attachments(org_id=test_config.main_org) == []

    def test_get_organisation(self, thehive_admin: TheHiveApi, test_config: TestConfig):
        main_org = thehive_admin.organisation.get(org_id=test_config.main_org)

        assert main_org["name"] == test_config.main_org

    def test_find_organisations(
        self, thehive_admin: TheHiveApi, test_config: TestConfig
    ):
        organisations = thehive_admin.organisation.find(
            filters=Eq("name", test_config.main_org)
        )

        assert len(organisations) == 1

    # most of the other organisation endpoints cannot be tested due to constraints
    # as at the moment the community license allows up to maximum 1 organisation
