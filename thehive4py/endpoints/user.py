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
        return self._session.make_request("POST", path="/api/v1/user", json=user)

    def get(self, user_id: str) -> OutputUser:
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}")

    def get_current(self) -> OutputUser:
        return self._session.make_request("GET", path="/api/v1/user/current")

    def delete(self, user_id: str, organisation: Optional[str] = None) -> None:
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/user/{user_id}/force",
            params={"organisation": organisation},
        )

    def update(self, user_id: str, fields: InputUpdateUser) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/user/{user_id}", json=fields
        )

    def lock(self, user_id: str) -> None:
        return self.update(user_id=user_id, fields={"locked": True})

    def unlock(self, user_id: str) -> None:
        return self.update(user_id=user_id, fields={"locked": False})

    def set_organisations(
        self, user_id: str, organisations: List[InputUserOrganisation]
    ) -> List[OutputUserOrganisation]:
        return self._session.make_request(
            "PUT",
            path=f"/api/v1/user/{user_id}/organisations",
            json={"organisations": organisations},
        )["organisations"]

    def set_password(self, user_id: str, password: str) -> None:
        return self._session.make_request(
            "POST",
            path=f"/api/v1/user/{user_id}/password/set",
            json={"password": password},
        )

    def get_apikey(self, user_id: str) -> str:
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}/key")

    def remove_apikey(self, user_id: str) -> None:
        return self._session.make_request("DELETE", path=f"/api/v1/user/{user_id}/key")

    def renew_apikey(self, user_id: str) -> str:
        return self._session.make_request(
            "POST", path=f"/api/v1/user/{user_id}/key/renew"
        )

    def get_avatar(self, user_id: str):
        # TODO: implement the avatar download
        raise NotImplementedError()

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputUser]:
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
