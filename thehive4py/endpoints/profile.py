from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.profile import InputProfile, InputUpdateProfile, OutputProfile


class ProfileEndpoint(EndpointBase):
    def create(self, profile: InputProfile) -> OutputProfile:
        """
        Create a new profile.

        Parameters:
            - profile (InputProfile): The data for the new profile.

        Returns:
            - OutputProfile: The created profile.
        """
        return self._session.make_request("POST", path="/api/v1/profile", json=profile)

    def get(self, profile_id: str) -> OutputProfile:
        """
        Get an existing profile.

        Parameters:
            - profile_id (str): The ID of the profile to get.

        Returns:
            - OutputProfile: The retrieved profile.

        """
        return self._session.make_request("GET", path=f"/api/v1/profile/{profile_id}")

    def delete(self, profile_id: str) -> None:
        """
        Delete an existing profile.

        Parameters:
            - profile_id (str): The ID of the profile to delete.

        Returns:
            None
        """
        return self._session.make_request("DELETE", f"/api/v1/profile/{profile_id}")

    def update(self, profile_id: str, fields: InputUpdateProfile) -> None:
        """
        Update an existing profile.

        Parameters:
            - profile_id (str): The ID of the profile to update.
            - fields (InputUpdateProfile): The fields to update.

        Returns:
            None
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
        """
        Find profiles matching the given filters, sort expressions and pagination.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.
            - sortby (SortExpr, optional): The sorting criteria to apply to the search.
            - paginate (Paginate, optional): The pagination settings to apply to the search.

        Returns:
            - List[OutputProfile]: The matching profiles.
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
        """
        Count profiles matching the given filters.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.

        Returns:
            - int: The number of matching profiles.
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
