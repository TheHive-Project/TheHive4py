from pathlib import Path

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.types.case import OutputCase


class TestMISPEndpoint:
    def test_get_status(self, thehive: TheHiveApi):
        status = thehive.misp.get_status()
        assert status["status"] == {}
        assert status["syncInProgress"] is False

    def test_sync(self, thehive_admin: TheHiveApi):
        response = thehive_admin.misp.sync()
        assert response == ""

    def test_export_case(self, thehive: TheHiveApi, test_case: OutputCase):
        misp_name = "non-existent-misp"
        with pytest.raises(
            TheHiveError, match=f"NotFoundError - MISP server {misp_name} not found"
        ):
            thehive.misp.export_case(case_id=test_case["_id"], misp_name=misp_name)

    def test_import_case(self, thehive: TheHiveApi, tmp_path: Path):
        import_path = str(tmp_path / "dummy-misp-event.json")
        with open(import_path, "w") as import_fp:
            import_fp.write("{}")

        with pytest.raises(
            TheHiveError, match="BadRequest - Could not convert json to MISP event"
        ):
            thehive.misp.import_case(import_case={}, import_path=import_path)
