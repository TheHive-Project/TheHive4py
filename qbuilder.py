"""

query:
    selector: required
    filter: optional
    sort: optional
    pagination: optional

state machine:

    selector -> filter -> sort -> pagination
    selector -> filter -> pagination
    selector -> filter -> selector
    selector -> sort -> pagination
    selector -> pagination


from thehive4py import TheHiveApi

hive = TheHiveApi(
    url="http://localhost:32770",
    username="admin",
    password="secret",
)


case_observables = hive.query.run(
    query=[
        {"_name": "listCase"},
        {
            "_name": "filter",
            "_gte": {
                "_field": "_createdAt",
                "_value": {
                    "amount": 1,
                    "unit": "days",
                    "look": "behind",
                    "modifier": "startOfDay",
                },
            },
        },
        {"_name": "observables"},
    ]
)


case_domain_observables = hive.query.run(
    query=[
        {"_name": "listCase"},
        {
            "_name": "filter",
            "_gte": {
                "_field": "_createdAt",
                "_value": {
                    "amount": 1,
                    "unit": "days",
                    "look": "behind",
                    "modifier": "startOfDay",
                },
            },
        },
        {
            "_name": "sort",
            "_fields": [
                {"_createdAt": "asc"},
            ],
        },
        {
            "_name": "filter",
            "_gte": {
                "_field": "_createdAt",
                "_value": {
                    "amount": 60,
                    "unit": "minutes",
                    "look": "behind",
                },
            },
        },
        {"_name": "observables"},
        {
            "_name": "filter",
            "_eq": {
                "_field": "dataType",
                "_value": "domain",
            },
        },
        {
            "_name": "sort",
            "_fields": [
                {"_createdAt": "asc"},
            ],
        },
        {
            "_name": "page",
            "from": 0,
            "to": 1,
        },
    ]
)

"""

from copy import deepcopy
from email.mime import base
from typing import Self

from thehive4py.query.filters import Eq, Gte
from thehive4py.query.page import Paginate
from thehive4py.query.sort import Asc


class SelectQuery:
    def __init__(
        self,
        name: str,
        id_or_name: str | None = None,
        base_query: list[dict] | None = None,
    ) -> None:
        self.query: list[dict]
        if base_query is None:
            self.query = []
        else:
            self.query = deepcopy(base_query)
        if id_or_name is None:
            self.query.append({"_name": name})
        else:
            self.query.append({"_name": name, "_idOrName": id_or_name})

    def select(self, name: str, id_or_name: str | None = None):
        return SelectQuery(
            name=name,
            id_or_name=id_or_name,
            base_query=self.query,
        )

    def filter(self, filter_expr: dict):
        return FilterQuery(filter_expr=filter_expr, base_query=self.query)

    def sort(self, sort_expr: dict):
        return SortQuery(sort_expr=sort_expr, base_query=self.query)

    def page(self, page_expr: dict):
        return PageQuery(page_expr=page_expr, base_query=self.query)


class FilterQuery:
    def __init__(self, filter_expr: dict, base_query: list[dict]) -> None:
        self.query = deepcopy(base_query)
        self.query.append({"_name": "filter", **filter_expr})

    def select(self, name: str, id_or_name: str | None = None):
        return SelectQuery(
            name=name,
            id_or_name=id_or_name,
            base_query=self.query,
        )

    def sort(self, sort_expr: dict):
        return SortQuery(sort_expr=sort_expr, base_query=self.query)

    def page(self, page_expr: dict):
        return PageQuery(page_expr=page_expr, base_query=self.query)


class SortQuery:
    def __init__(
        self,
        sort_expr: dict,
        base_query: list[dict],
    ) -> None:
        self.query = deepcopy(base_query)
        self.query.append({"_name": "sort", **sort_expr})

    def page(self, page_expr: dict):
        return PageQuery(page_expr=page_expr, base_query=self.query)


class PageQuery:
    def __init__(
        self,
        page_expr: dict,
        base_query: list[dict],
    ) -> None:
        self.query = deepcopy(base_query)
        self.query.append({"_name": "page", **page_expr})


def print_query(query_instance):
    import json

    print(json.dumps(query_instance.query, indent=4))
    print("-----")


def QueryBuilder(name: str, id_or_name: str | None = None):
    return SelectQuery(name=name, id_or_name=id_or_name)


print("Raw query expressions")
q = QueryBuilder(name="listCase")
print_query(q)
q = q.filter({"_gte": {"_field": "_createdAt", "_value": 1234567890}})
print_query(q)
q = q.select("observables")
print_query(q)
q = q.filter({"_eq": {"_field": "dataType", "_value": "domain"}})
print_query(q)
q = q.sort({"_fields": [{"_createdAt": "asc"}]})
print_query(q)
q = q.page({"from": 0, "to": 2, "extraData": []})

print("Helper query expressions")
q2 = (
    QueryBuilder(name="listCase")
    .filter(Gte(field="_createdAt", value=1234567890))
    .select("observables")
    .filter(Eq(field="dataType", value="domain"))
    .sort(Asc(field="_createdAt"))
    .page(Paginate(start=0, end=2))
)
print_query(q2)


print(q.query == q2.query)


from thehive4py import TheHiveApi

hive = TheHiveApi(
    url="http://localhost:32770",
    username="admin",
    password="secret",
)

result = hive.query.run(query=q.query)
print(result)
print(len(result))
