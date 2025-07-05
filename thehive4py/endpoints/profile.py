from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.profile import InputProfile, InputUpdateProfile, OutputProfile


class ProfileEndpoint(EndpointBase):
    def create(self, profile: InputProfile) -> OutputProfile:
        """Create a profile.

        Args:
            profile: The body of the profile.

        Returns:
            The created profile.
        """
        return self._session.make_request("POST", path="/api/v1/profile", json=profile)

    def get(self, profile_id: str) -> OutputProfile:
        """Get a profile by id.

        Args:
            profile_id: The id of the profile.

        Returns:
            The profile specified by the id.
        """
        return self._session.make_request("GET", path=f"/api/v1/profile/{profile_id}")

    def delete(self, profile_id: str) -> None:
        """Delete a profile.

        Args:
            profile_id: The id of the profile.

        Returns:
            N/A
        """
        return self._session.make_request("DELETE", f"/api/v1/profile/{profile_id}")

    def update(self, profile_id: str, fields: InputUpdateProfile) -> None:
        """Update a profile.

        Args:
            profile_id: The id of the profile.
            fields: The fields of the profile to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", f"/api/v1/profile/{profile_id}", json=fields
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProfile]:
        """Find multiple profiles.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of profiles matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listProfile"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "profiles"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        """Count profiles.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of profiles matched by the query.
        """
        query: QueryExpr = [
            {"_name": "listProfile"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "profile.count"},
            json={"query": query},
        )
