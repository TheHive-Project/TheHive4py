import typing

from thehive4py.endpoints._base import EndpointBase


class QueryEndpoint(EndpointBase):
    def run(
        self, query: typing.List[dict], exclude_fields: typing.List[str] = []
    ) -> typing.Any:
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query, "excludeFields": exclude_fields},
        )
