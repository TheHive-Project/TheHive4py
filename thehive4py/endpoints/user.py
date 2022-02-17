from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.user import InputUser, OutputUser


class UserEndpoint(EndpointBase):
    def create(self, user: InputUser) -> OutputUser:
        return self._session.make_request("POST", path="/api/v1/user", json=user)

    def get(self, user_id: str) -> OutputUser:
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}")

    def get_current(self) -> OutputUser:
        return self._session.make_request("GET", path="/api/v1/user/current")

    def delete(self, user_id: str, organisation: str = None) -> None:
        self._session.make_request(
            "DELETE",
            path=f"/api/v1/user/{user_id}/force",
            params={"organisation": organisation},
        )

    def update(self, user_id: str, fields: dict) -> None:
        self._session.make_request("PATCH", path=f"/api/v1/user/{user_id}", json=fields)

    def lock(self, user_id: str) -> None:
        self.update(user_id=user_id, fields={"locked": True})

    def unlock(self, user_id: str) -> None:
        self.update(user_id=user_id, fields={"locked": False})

    def set_password(self, user_id: str, password: str) -> None:
        self._session.make_request(
            "POST",
            path=f"/api/v1/user/{user_id}/password/set",
            json={"password": password},
        )

    def get_apikey(self, user_id: str) -> str:
        return self._session.make_request("GET", path=f"/api/v1/user/{user_id}/key")

    def remove_apikey(self, user_id: str) -> None:
        self._session.make_request("DELETE", path=f"/api/v1/user/{user_id}/key")

    def renew_apikey(self, user_id: str) -> str:
        return self._session.make_request(
            "POST", path=f"/api/v1/user/{user_id}/key/renew"
        )

    def find(
        self,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
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

    def count(self, filters: FilterExpr = None) -> int:
        query: QueryExpr = [
            {"_name": "listUser"},
            {"_name": "limitedCount"},
            *self._build_subquery(filters=filters),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "cases.count"},
            json={"query": query},
        )
