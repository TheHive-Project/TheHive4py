from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.user import (
    InputUpdateUser,
    InputUser,
    InputUserOrganisation,
    OutputUser,
    OutputUserOrganisation,
)


class UserEndpoint(EndpointBase):
    def create(self, user: InputUser) -> OutputUser:
        """
        Creates a new user.

        Parameters:
            - user (InputUser): The data for the new user.

        Returns:
            - OutputUser: The created profile.
        """
        return self._session.make_request("POST", path="/api/v1/user", json=user)

    def get(self, user_id: str) -> OutputUser:
        """
        Gets an existing user.

        Parameters:
            - user_id (str): The ID of the user to get.

        Returns:
            - OutputUser: The retrieved user.

        """
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}")

    def get_current(self) -> OutputUser:
        """
        Gets the current user.

        Returns:
            - OutputUser: The current user.

        """
        return self._session.make_request("GET", path="/api/v1/user/current")

    def delete(self, user_id: str, organisation: Optional[str] = None) -> None:
        """
        Deletes an existing user.

        Parameters:
            - user_id (str): The ID of the user to delete.
            - organisation (Optional[str]): The user's organisation.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/user/{user_id}/force",
            params={"organisation": organisation},
        )

    def update(self, user_id: str, fields: InputUpdateUser) -> None:
        """
        Update an existing user.

        Parameters:
            - user_id (str): The ID of the user to update.
            - fields (InputUpdateUser): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/user/{user_id}", json=fields
        )

    def lock(self, user_id: str) -> None:
        """
        Locks the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user to be locked.

        Returns:
            None
        """
        return self.update(user_id=user_id, fields={"locked": True})

    def unlock(self, user_id: str) -> None:
        """
        Unlocks the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user to be unlocked.

        Returns:
            None
        """
        return self.update(user_id=user_id, fields={"locked": False})

    def set_organisations(
        self, user_id: str, organisations: List[InputUserOrganisation]
    ) -> List[OutputUserOrganisation]:
        """
        Sets the list of organisations for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose organisations will be set.
            - organisations (List[InputUserOrganisation]): A list of `InputUserOrganisation` objects representing the organisations to be set.

        Returns:
            - List[OutputUserOrganisation]: A list of `OutputUserOrganisation` objects representing the updated organisations.
        """
        return self._session.make_request(
            "PUT",
            path=f"/api/v1/user/{user_id}/organisations",
            json={"organisations": organisations},
        )["organisations"]

    def set_password(self, user_id: str, password: str) -> None:
        """
        Sets the password for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose password will be set.
            - password (str): The new password to be set.

        Returns:
            None
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/user/{user_id}/password/set",
            json={"password": password},
        )

    def get_apikey(self, user_id: str) -> str:
        """
        Retrieves the API key for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose API key will be retrieved.

        Returns:
            - str: The API key for the user.
        """
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}/key")

    def remove_apikey(self, user_id: str) -> None:
        """
        Removes the API key for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose API key will be removed.

        Returns:
            None
        """
        return self._session.make_request("DELETE", path=f"/api/v1/user/{user_id}/key")

    def renew_apikey(self, user_id: str) -> str:
        """
        Renews the API key for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose API key will be renewed.

        Returns:
            - str: The new API key for the user.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/user/{user_id}/key/renew"
        )

    def get_avatar(self, user_id: str):
        """
        Retrieves the avatar for the user with the given `user_id`.

        Parameters:
            - user_id (str): The ID of the user whose avatar will be retrieved.

        Raises:
            NotImplementedError: This method is not implemented yet.

        """
        # TODO: implement the avatar download
        raise NotImplementedError()

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputUser]:
        """
        Find users matching the given filters, sort expressions and pagination.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.
            - sortby (SortExpr, optional): The sorting criteria to apply to the search.
            - paginate (Paginate, optional): The pagination settings to apply to the search.

        Returns:
            - List[OutputUser]: The matching users.
        """
        query: QueryExpr = [
            {"_name": "listUser"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "users"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        """
        Count users matching the given filters.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.

        Returns:
            - int: The number of matching users.
        """
        query: QueryExpr = [
            {"_name": "listUser"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "cases.count"},
            json={"query": query},
        )
