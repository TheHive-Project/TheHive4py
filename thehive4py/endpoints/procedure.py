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
    def create_in_alert(
        self, alert_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """
        Create a procedure for a given alert.

        Parameters:
            - alert_id (str): The ID or name of the alert to create the procedure for.
            - procedure (InputProcedure): The procedure to create.

        Returns:
            - OutputProcedure: The created procedure.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/procedure", json=procedure
        )

    def create_in_case(
        self, case_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """
        Create a new procedure associated with the specified case.

        Parameters:
            - case_id (str): The ID of the case to create the procedure for.
            - procedure (InputProcedure): The procedure to create.

        Returns:
            - OutputProcedure: The procedure that was created.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/procedure", json=procedure
        )

    def get(self, procedure_id: str) -> OutputProcedure:
        """
        Retrieves a procedure.

        Parameters:
            - procedure_id (str): The ID of the procedure to search for.

        Returns:
            - OutputProcedure: The retrieved procedure.
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

    def delete(self, procedure_id: str) -> None:
        """
        Deletes a procedure.

        Parameters:
            - procedure_id (str): The ID of the procedure to delete.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/procedure/{procedure_id}"
        )

    def update(self, procedure_id: str, fields: InputUpdateProcedure) -> None:
        """
        Update an existing procedure.

        Parameters:
            - procedure_id (str): The ID of the procedure to update.
            - fields (InputUpdateProcedure): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/procedure/{procedure_id}", json=fields
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProcedure]:

        """
        Finds procedures based on filters, sort experssions and pagination.

        Parameters:
            - filters (Optional[FilterExpr]): A filter expression to filter the procedures by.
            - sortby (Optional[SortExpr]): A sort expression to sort the procedures by.
            - paginate (Optional[Paginate]): A pagination object to limit and offset the results.

        Returns:
            - List[OutputProcedure]: A list of procedures associated with the given case.
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
