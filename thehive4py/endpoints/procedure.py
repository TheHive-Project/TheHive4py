from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.procedure import (
    InputProcedure,
    InputUpdateProcedure,
    OutputProcedure,
)


class ProcedureEndpoint(EndpointBase):
    def create_in_case(
        self, case_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """Create a procedure in a case.

        Args:
            case_id: The id of the case.
            procedure: The fields of the procedure to create.

        Returns:
            The created procedure.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/procedure", json=procedure
        )

    def bulk_create_in_case(
        self, case_id: str, procedures: List[InputProcedure]
    ) -> List[OutputProcedure]:
        """Create several procedures in a case.

        Args:
            case_id: The id of the case.
            procedures: The list of procedures to create.

        Returns:
            The list of created procedures.
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/case/{case_id}/procedures",
            json={"procedures": procedures},
        )

    def create_in_alert(
        self, alert_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """Create a procedure in an alert.

        Args:
            alert_id: The id of the alert.
            procedure: The fields of the procedure to create.

        Returns:
            The created procedure.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/procedure", json=procedure
        )

    def bulk_create_in_alert(
        self, alert_id: str, procedures: List[InputProcedure]
    ) -> List[OutputProcedure]:
        """Create multiple procedures in an alert.

        Args:
            alert_id: The id of the alert.
            procedures: The list of procedures to create.

        Returns:
            The list of created procedures.
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/alert/{alert_id}/procedures",
            json={"procedures": procedures},
        )

    def delete(self, procedure_id: str) -> None:
        """Delete a procedure.

        Args:
            procedure_id: The id of the procedure.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/procedure/{procedure_id}"
        )

    def update(self, procedure_id: str, fields: InputUpdateProcedure) -> None:
        """Update a procedure.

        Args:
            procedure_id: The id of the procedure.
            fields: The fields of the procedure to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/procedure/{procedure_id}", json=fields
        )

    def bulk_delete(self, procedure_ids: List[str]) -> None:
        """Delete multiple procedures.

        Args:
            procedure_ids: The list of procedure ids to delete.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST",
            path="/api/v1/procedure/delete/_bulk",
            json={"ids": procedure_ids},
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProcedure]:
        """Find multiple procedures.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of procedures matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listProcedure"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "procedures"},
            json={"query": query},
        )

    def get(self, procedure_id: str) -> OutputProcedure:
        """Get a procedure by id.

        Args:
            procedure_id: The id of the procedure.

        Returns:
            The procedure specified by the id.
        """
        # TODO: temp implementation until a dedicated get endpoint
        procedures = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": [{"_name": "getProcedure", "idOrName": procedure_id}]},
        )
        try:
            return procedures[0]
        except IndexError:
            raise TheHiveError("404 - Procedure not found")
