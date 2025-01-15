from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.case_template import OutputCaseTemplate, InputCaseTemplate
from typing import List, Optional


class CaseTemplateEndpoint(EndpointBase):
    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputCaseTemplate]:
        query: QueryExpr = [
            {"_name": "listCaseTemplate"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query},
            params={"name": "caseTemplate"},
        )

    def get(self, case_template_id: str) -> OutputCaseTemplate:
        return self._session.make_request(
            "GET", path=f"/api/v1/caseTemplate/{case_template_id}"
        )

    def create(self, case_template: InputCaseTemplate) -> OutputCaseTemplate:
        return self._session.make_request(
            "POST", path="/api/v1/caseTemplate", json=case_template
        )

    def delete(self, case_template_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/caseTemplate/{case_template_id}"
        )

    def update(self, case_template_id: str, fields: InputCaseTemplate) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/caseTemplate/{case_template_id}", json=fields
        )
