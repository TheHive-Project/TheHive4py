import warnings
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
    def get_current(self) -> OutputUser:
        """Get the current session's user.

        Returns:
            The current session user.
        """
        return self._session.make_request("GET", path="/api/v1/user/current")

    def create(self, user: InputUser) -> OutputUser:
        """Create a user.

        Args:
            user: The body of the user.

        Returns:
            The created user.
        """
        return self._session.make_request("POST", path="/api/v1/user", json=user)

    def get(self, user_id: str) -> OutputUser:
        """Get a user by id.

        Args:
            user_id: The id of the user.

        Returns:
            The user specified by the id.
        """
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}")

    def lock(self, user_id: str) -> None:
        """Lock a user.

        !!! warning
            Deprecated: use the generic [user.update]
            [thehive4py.endpoints.user.UserEndpoint.update] method
            to set the `locked` field to `True`

        Args:
            user_id: The id of the user.

        Returns:
            N/A
        """
        warnings.warn(
            message=(
                "Deprecated: use the generic user.update method to "
                "set the `locked` field to True"
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        return self.update(user_id=user_id, fields={"locked": True})

    def unlock(self, user_id: str) -> None:
        """Unlock a user.

        !!! warning
            Deprecated: use the generic [user.update]
            [thehive4py.endpoints.user.UserEndpoint.update] method
            to set the `locked` field to `False`

        Args:
            user_id: The id of the user.

        Returns:
            N/A
        """
        warnings.warn(
            message=(
                "Deprecated: use the generic user.update method to "
                "set the `locked` field to False"
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        return self.update(user_id=user_id, fields={"locked": False})

    def update(self, user_id: str, fields: InputUpdateUser) -> None:
        """Update a user.

        Args:
            user_id: The id of the user.
            fields: The fields of the user to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/user/{user_id}", json=fields
        )

    def delete(self, user_id: str, organisation: Optional[str] = None) -> None:
        """Delete a user.

        Args:
            user_id: The id of the user.
            organisation: The organisation from which the user should be deleted.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/user/{user_id}/force",
            params={"organisation": organisation},
        )

    def set_organisations(
        self, user_id: str, organisations: List[InputUserOrganisation]
    ) -> List[OutputUserOrganisation]:
        """Set the organisations of a user.

        Args:
            user_id: The id of the user.
            organisations: The list of organisations to set to the user.

        Returns:
            The list of the set user organisations.
        """
        return self._session.make_request(
            "PUT",
            path=f"/api/v1/user/{user_id}/organisations",
            json={"organisations": organisations},
        )["organisations"]

    def set_password(self, user_id: str, password: str) -> None:
        """Set the password of a user.

        Args:
            user_id: The id of the user.
            password: The new password of the user.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/user/{user_id}/password/set",
            json={"password": password},
        )

    def change_password(
        self, user_id: str, password: str, current_password: str
    ) -> None:
        """Change the password of a user.

        Args:
            user_id: The id of the user.
            password: The new password of the user.
            current_password: The old password of the user.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/user/{user_id}/password/change",
            json={"password": password, "currentPassword": current_password},
        )

    def get_apikey(self, user_id: str) -> str:
        """Get the apikey of a user.

        Args:
            user_id: The id of the user.

        Returns:
            The apikey of the user.
        """
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}/key")

    def remove_apikey(self, user_id: str) -> None:
        """Remove the apikey of a user.

        Args:
            user_id: The id of the user.

        Returns:
            N/A
        """
        return self._session.make_request("DELETE", path=f"/api/v1/user/{user_id}/key")

    def renew_apikey(self, user_id: str) -> str:
        """Renew the apikey of a user.

        Args:
            user_id: The id of the user.

        Returns:
            The renewed apikey of the user.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/user/{user_id}/key/renew"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputUser]:
        """Find multiple users.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of users matched by the query or an empty list.
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
        """Count users.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of users matched by the query.
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
