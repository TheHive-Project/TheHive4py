import json as jsonlib

from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.case import OutputCase
from thehive4py.types.misp import InputMISPImportCase, OutputMISPStatus


class MISPEndpoint(EndpointBase):
    def get_status(self) -> OutputMISPStatus:
        """Get MISP status.

        Returns:
            The status of the MISP connector.
        """
        return self._session.make_request("GET", path="/api/v1/connector/misp/status")

    def sync(self) -> None:
        """Sync with MISP servers.

        Returns:
            N/A
        """
        return self._session.make_request(
            "GET", path="/api/v1/connector/misp/_syncAlerts"
        )

    def export_case(self, case_id: str, misp_name: str) -> None:
        """Export a case to MISP.

        Args:
            case_id: The id of the case to export.
            misp_name: The name of the MISP server to export to.
        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/connector/misp/export/{case_id}/{misp_name}"
        )

    def import_case(
        self, import_case: InputMISPImportCase, import_path: str
    ) -> OutputCase:
        """Import a case from MISP.

        Args:
            import_case: The metadata of the MISP case import.

        Returns:
            The imported case.
        """

        return self._session.make_request(
            "POST",
            path="/api/v1/connector/misp/case/import",
            data={"_json": jsonlib.dumps(import_case)},
            files={"file": self._fileinfo_from_filepath(import_path)},
        )
