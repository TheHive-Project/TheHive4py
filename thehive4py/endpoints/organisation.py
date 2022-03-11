from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.organisation import (
    InputBulkOrganisationLink,
    InputOrganisation,
    InputOrganisationLink,
    InputUpdateOrganisation,
    OutputOrganisation,
    OutputSharingProfile,
)


class OrganisationEndpoint(EndpointBase):
    def create(self, organisation: InputOrganisation) -> OutputOrganisation:
        return self._session.make_request(
            "POST", path="/api/v1/organisation", json=organisation
        )

    def get(self, org_id: str) -> OutputOrganisation:
        return self._session.make_request("GET", path=f"/api/v1/organisation/{org_id}")

    def update(self, org_id: str, fields: InputUpdateOrganisation) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/organisation/{org_id}", json=fields
        )

    def delete(self, org_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/organisation/{org_id}"
        )

    def link(self, org_id: str, other_org_id: str, link: InputOrganisationLink) -> None:
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}", json=link
        )

    def unlink(self, org_id: str, other_org_id: str) -> None:
        return self._session.make_request(
            "GET", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}"
        )

    def list_links(self, org_id: str) -> List[OutputOrganisation]:
        return self._session.make_request(
            "GET", path=f"/api/v1/organisation/{org_id}/links"
        )

    def bulk_link(self, org_id: str, links: List[InputBulkOrganisationLink]) -> None:
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/links", json={"links": links}
        )

    def list_sharing_profiles(self) -> List[OutputSharingProfile]:
        return self._session.make_request("GET", path="/api/v1/sharingProfile")

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputOrganisation]:
        query: QueryExpr = [
            {"_name": "listOrganisation"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "organisations"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        query: QueryExpr = [
            {"_name": "listOrganisation"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "organisations.count"},
            json={"query": query},
        )
