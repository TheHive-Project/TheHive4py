import typing

from thehive4py.endpoints._base import EndpointBase


class QueryEndpoint(EndpointBase):
    def run(
        self, query: typing.List[dict], exclude_fields: typing.List[str] = []
    ) -> typing.Any:
        """Run any arbitrary queries using TheHive's Query API.

        This method provides low level access to the Query API to be able to run
        any queries.
        More information on the supported features  can be found
        [here](https://docs.strangebee.com/thehive/api-docs/#tag/Query-and-Export/operation/Query%20API).

        """
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query, "excludeFields": exclude_fields},
        )
