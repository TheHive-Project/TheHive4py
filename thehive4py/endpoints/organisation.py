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
        """
        Creates a new organisaation in TheHive.

        Parameters:
            - organisation (InputOrganisation): The org to create.

        Returns:
            - OutputOrganisation: The created org.
        """
        return self._session.make_request(
            "POST", path="/api/v1/organisation", json=organisation
        )

    def get(self, org_id: str) -> OutputOrganisation:
        """
        Retrieves an existing org from TheHive.

        Parameters:
            - org_id (str): The ID of the org to retrieve.

        Returns:
            - OutputOrganisation: The retrieved org.
        """
        return self._session.make_request("GET", path=f"/api/v1/organisation/{org_id}")

    def update(self, org_id: str, fields: InputUpdateOrganisation) -> None:
        """
        Updates an existing org in TheHive.

        Parameters:
            - org_id (str): The ID of the org to update.
            - fields (InputUpdateOrganisation): The updated org.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/organisation/{org_id}", json=fields
        )

    def delete(self, org_id: str) -> None:
        """
        Deletes an existing org from TheHive.

        Parameters:
            - org_id (str): The ID of the org to delete.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/organisation/{org_id}"
        )

    def link(self, org_id: str, other_org_id: str, link: InputOrganisationLink) -> None:
        """
        Link between organisations.

        Parameters:
            - org_id (str): The ID of the org to link.
            - other_org_id (str): The ID of the org to link with.
            - link (InputOrganisationLink): the link between the orgs.

        Returns:
            None
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}", json=link
        )

    def unlink(self, org_id: str, other_org_id: str) -> None:
        """
        Remove a link between organisations.

        Parameters:
            - org_id (str): The ID of the org to unlink.
            - other_org_id (str): The ID of the org to unlink from.

        Returns:
            None
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}"
        )

    def list_links(self, org_id: str) -> List[OutputOrganisation]:
        """
        Get a list of orgs linked to the specified org.

        Parameters:
            - org_id (str): The ID of the org to get linked orgs for.

        Returns:
            - List[OutputOrganisation]: A list of OutputOrganisation objects representing the linked orgs.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/organisation/{org_id}/links"
        )

    def bulk_link(self, org_id: str, links: List[InputBulkOrganisationLink]) -> None:
        """
        Adds or updates multiple links for an organization.

        Parameters:
            - org_id (str): The ID of the organization to add or update the links for.
            - links (List[InputBulkOrganisationLink]): A list of link objects to add or update.

        Returns:
            None
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/links", json={"links": links}
        )

    def list_sharing_profiles(self) -> List[OutputSharingProfile]:
        """
        Retrieves a list of sharing profiles.

        Returns:
            - List[OutputSharingProfile]: A list of OutputSharingProfile objects containing information about the sharing profiles.
        """
        return self._session.make_request("GET", path="/api/v1/sharingProfile")

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputOrganisation]:
        """
        Find orgs based on the specified filters, sort order, and pagination.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.
            - sortby (Optional[SortExpr]): The sort order to apply to the results.
            - paginate (Optional[Paginate]): The pagination parameters to apply to the query.

        Returns:
            - List[OutputOrganisation]: A list of matching orgs.
        """
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
        """
        Count the number of orgs that match the specified filters.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.

        Returns:
            - int: The number of matching orgs.
        """
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
