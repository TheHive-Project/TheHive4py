from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.case_template import InputCaseTemplate, OutputCaseTemplate
from thehive4py.types.page_template import OutputPageTemplate


class CaseTemplateEndpoint(EndpointBase):
    def create(self, case_template: InputCaseTemplate) -> OutputCaseTemplate:
        """Create a case template.

        Args:
            case_template: The body of the case template.

        Returns:
            The created case template.
        """
        return self._session.make_request(
            "POST", path="/api/v1/caseTemplate", json=case_template
        )

    def get(self, case_template_id: str) -> OutputCaseTemplate:
        """Get a case template by id.

        Args:
            case_template_id: The id of the case template.

        Returns:
            The case template specified by the id.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/caseTemplate/{case_template_id}"
        )

    def delete(self, case_template_id: str) -> None:
        """Delete a case template.

        Args:
            case_template_id: The id of the case template.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/caseTemplate/{case_template_id}"
        )

    def update(self, case_template_id: str, fields: InputCaseTemplate) -> None:
        """Update a case template.

        Args:
            case_template_id: The id of the case template.
            fields: The fields of the case template to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/caseTemplate/{case_template_id}", json=fields
        )

    def link_page_templates(
        self, case_template_id: str, page_template_ids: List[str]
    ) -> None:
        """Link page templates to a case template.

        Args:
            case_template_id: The id or name of the case template.
            page_template_ids: The list of page template ids to link.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PUT",
            path=f"/api/v1/caseTemplate/{case_template_id}/pageTemplate/link",
            json={"pageTemplateIds": page_template_ids},
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputCaseTemplate]:
        """Find multiple case templates.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of case templates matched by the query or an empty list.
        """
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

    def find_page_templates(
        self,
        case_template_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputPageTemplate]:
        """Find page templates related to a case template.

        Args:
            case_template_id: The case template id.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of page templates matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCaseTemplate", "idOrName": case_template_id},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
            {"_name": "pageTemplates"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query},
            params={"name": "pageTemplate"},
        )
