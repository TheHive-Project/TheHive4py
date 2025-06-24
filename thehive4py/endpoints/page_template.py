from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.page_template import (
    InputPageTemplate,
    InputUpdatePageTemplate,
    OutputPageTemplate,
)


class PageTemplateEndpoint(EndpointBase):
    def create(self, page_template: InputPageTemplate) -> OutputPageTemplate:
        """Create a page template.

        Args:
            page_template: The body of the page template.

        Returns:
            The created page template.
        """
        return self._session.make_request(
            "POST", path="/api/v1/pageTemplate", json=page_template
        )

    def delete(self, page_template_id: str) -> None:
        """Delete a page template.

        Args:
            page_template_id: The id of the page template.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/pageTemplate/{page_template_id}"
        )

    def update(self, page_template_id: str, fields: InputUpdatePageTemplate) -> None:
        """Update a page template.

        Args:
            page_template_id: The id of the page template.
            fields: The fields of the page template to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/pageTemplate/{page_template_id}", json=fields
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputPageTemplate]:
        """Find multiple page templates.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of page templates matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listPageTemplate"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query},
            params={"name": "listPageTemplate"},
        )

    def get(self, page_template_id: str) -> OutputPageTemplate:
        """Get a page template by id.

        Args:
            page_template_id: The id of the page template.

        Returns:
            The page template specified by the id.
        """
        # TODO: temp implementation until a dedicated get endpoint [if ever ;)]
        page_templates = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={
                "query": [{"_name": "getPageTemplate", "idOrName": page_template_id}]
            },
        )

        if not page_templates:
            raise TheHiveError("404 - Page Template Not Found")

        return page_templates[0]
