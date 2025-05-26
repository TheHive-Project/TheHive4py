from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.attachment import OutputAttachment
from thehive4py.types.organisation import (
    InputBulkOrganisationLink,
    InputOrganisation,
    InputOrganisationLink,
    InputUpdateOrganisation,
    OutputOrganisation,
    OutputOrganisationLink,
    OutputSharingProfile,
)


class OrganisationEndpoint(EndpointBase):
    def add_attachment(
        self, attachment_paths: List[str], can_rename: bool = True
    ) -> List[OutputAttachment]:
        """Add attachment to organisation.

        Args:
            attachment_paths: List of paths to the attachments to create.
            can_rename: If set to True, the files can be renamed if they already exist
                with the same name

        Returns:
            The created attachments.
        """
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", "/api/v1/attachment", data={"canRename": can_rename}, files=files
        )["attachments"]

    def delete_attachment(self, attachment_id: str) -> None:
        """Delete an attachment.

        Args:
            attachment_id: The id of the attachment.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/attachment/{attachment_id}"
        )

    def download_attachment(self, attachment_id: str, attachment_path: str) -> None:
        """Download an attachment.

        Args:
            attachment_id: The id of the attachment.
            attachment_path: The local path to download the attachment to.

        Returns:
            N/A
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/attachment/{attachment_id}/download",
            download_path=attachment_path,
        )

    def find_attachments(
        self,
        org_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAttachment]:
        """Find attachments related to an organisation.

        Args:
            org_id: The id of the organisation.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case attachments matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getOrganisation", "idOrName": org_id},
            {"_name": "attachments"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "organisation-attachments"},
            json={"query": query},
        )

    def create(self, organisation: InputOrganisation) -> OutputOrganisation:
        """Create an organisation.

        Args:
            organisation: The body of the organisation.

        Returns:
            The created organisation.
        """
        return self._session.make_request(
            "POST", path="/api/v1/organisation", json=organisation
        )

    def get(self, org_id: str) -> OutputOrganisation:
        """Get an organisation.

        Args:
            org_id: The id of the organisation.

        Returns:
            The organisation specified by the id.
        """
        return self._session.make_request("GET", path=f"/api/v1/organisation/{org_id}")

    def update(self, org_id: str, fields: InputUpdateOrganisation) -> None:
        """Get an organisation.

        Args:
            org_id: The id of the organisation.
            fields: The fields of the organisation to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/organisation/{org_id}", json=fields
        )

    def get_avatar(self, org_id: str, file_hash: str, avatar_path: str) -> None:
        """Get an organisaton avatar.

        Args:
            org_id: The id of the organisation.
            file_hash: The hash of the organisation avatar.
            avatar_path: The local path to download the organisation avatar to.

        Returns:
            N/A
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/organisation/{org_id}/avatar/{file_hash}",
            download_path=avatar_path,
        )

    def link(self, org_id: str, other_org_id: str, link: InputOrganisationLink) -> None:
        """Link two organisatons.

        Args:
            org_id: The id of the organisation.
            other_org_id: The id of the other organisation.
            link: The type of organisation links.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}", json=link
        )

    def unlink(self, org_id: str, other_org_id: str) -> None:
        """Unlink two organisatons.

        Args:
            org_id: The id of the organisation.
            other_org_id: The id of the other organisation.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/organisation/{org_id}/link/{other_org_id}"
        )

    def list_links(self, org_id: str) -> List[OutputOrganisationLink]:
        """List links of an organisatons.

        Args:
            org_id: The id of the organisation.

        Returns:
            The list of organisation links.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/organisation/{org_id}/links"
        )

    def bulk_link(self, org_id: str, links: List[InputBulkOrganisationLink]) -> None:
        """Bulk link organisations.

        Args:
            org_id: The id of the organisation.
            links: The list of organisation links.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/organisation/{org_id}/links", json={"links": links}
        )

    def list_sharing_profiles(self) -> List[OutputSharingProfile]:
        """List all sharing profiles.

        Returns:
            The list of sharing profiles.
        """
        return self._session.make_request("GET", path="/api/v1/sharingProfile")

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputOrganisation]:
        """Find multiple organisations.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of organisations matched by the query or an empty list.
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
        """Count organisations.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of organisations matched by the query.
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
