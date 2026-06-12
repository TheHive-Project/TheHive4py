import json
from collections import UserList
from copy import deepcopy
from typing import List, Literal, Optional, Self, Union

from thehive4py.query.filters import Eq, FilterExpr, Gte
from thehive4py.query.page import PageExpr, Paginate
from thehive4py.query.sort import Asc, Desc, SortExpr
from thehive4py.session import _SessionJSONEncoder

"""
TODO: figure out the proper naming convention for expressions:

{
    "query": [ 
        {"_name": "listCase" },              <-- SelectOperation ( ListOperation / GetOperation ? )
        {"_name": "filter", <filter-expr>}, <-- FilterOperation
        {"_name": "observables"},            <-- SelectOperation
        {"_name": "filter", <filter-expr>}, <-- FilterOperation
        {"_name": "sort", <sort-expr>},     <-- SortOperation
        {"_name": "page", <page-expr>},     <-- PageOperation
    ],                                  <-- QueryExpr
    "excludedFields": []
}


Introduce a list method for the endpoints and retire the find endpoints
The list method should utilize this builder to create the query 


Maybe rethink the XyzExpr = Union["_XyzBase", native-type] type variable
And reserve the XyzExpr for the class based expressions and don't give an option to the user
in the convenience list methods for native types, but only in the generic query endpoint

E.g.:

QueryExpr -> class
FilterExpr -> class

alert.list(filters=Eq(...) & Gte(...))  # supported
alert.list(filters={"_eq": {...}})  # not supported and throws a type error but technically would work


OOOOOR keep the union type like:

QueryExprLike = Union[QueryExpr, list]

SelectorExprLike = Union[SelectorExpr, dict]
FilterExprLike = Union[FilterExpr, dict]
SortExprLike = Union[SortExpr, dict]
PageExprLike = Union[PageExpr, dict]



"""


QueryExpr = Union["_QueryExprBase", list]

ListSelectors = Literal["listCase", "listAlert"]

GetSelectors = Literal["getCase", "getAlert"]


class _QueryExprBase:
    def __init__(self, init_query: Optional[List[dict]] = None):
        if init_query:
            self._data = deepcopy(init_query)
        else:
            self._data = []


class GetQuery(_QueryExprBase):
    def __init__(self, name: str, id_or_name: str):
        super().__init__(init_query=[{"_name": name, "_idOrName": id_or_name}])

    def select(self, name: str) -> "ListQuery":
        return ListQuery(
            name=name,
            init_query=self._data,
        )

    def page(self, page_expr: dict) -> "_PageQuery":
        return _PageQuery(page_expr=page_expr, init_query=self._data)


class ListQuery(_QueryExprBase):
    def __init__(
        self,
        name: str,
        init_query: Optional[List[dict]] = None,
    ) -> None:
        super().__init__(init_query=init_query)

        select_operation = {"_name": name}

        self._data.append(select_operation)

    def select(self, name: str) -> "ListQuery":
        return ListQuery(
            name=name,
            init_query=self._data,
        )

    def filter(self, filter_expr: FilterExpr) -> "_FilterQuery":
        return _FilterQuery(filter_expr=filter_expr, init_query=self._data)

    def sort(self, sort_expr: dict) -> "_SortQuery":
        return _SortQuery(sort_expr=sort_expr, init_query=self._data)

    def page(self, page_expr: dict) -> "_PageQuery":
        return _PageQuery(page_expr=page_expr, init_query=self._data)


class _FilterQuery(_QueryExprBase):
    def __init__(self, filter_expr: FilterExpr, init_query: List[dict]) -> None:
        filter_operation = {"_name": "filter", **filter_expr}
        super().__init__(init_query=[*init_query, filter_operation])

    def select(self, name: str) -> "ListQuery":
        return ListQuery(
            name=name,
            init_query=self._data,
        )

    def sort(self, sort_expr: SortExpr) -> "_SortQuery":
        return _SortQuery(sort_expr=sort_expr, init_query=self._data)

    def page(self, page_expr: PageExpr) -> "_PageQuery":
        return _PageQuery(page_expr=page_expr, init_query=self._data)


class _SortQuery(_QueryExprBase):
    def __init__(
        self,
        sort_expr: SortExpr,
        init_query: list[dict],
    ) -> None:
        sort_operation = {"_name": "sort", **sort_expr}
        super().__init__(init_query=[*init_query, sort_operation])

    def page(self, page_expr: PageExpr) -> "_PageQuery":
        return _PageQuery(page_expr=page_expr, init_query=self._data)


class _PageQuery(_QueryExprBase):
    def __init__(
        self,
        page_expr: PageExpr,
        init_query: List[dict],
    ) -> None:
        page_operation = {"_name": "page", **page_expr}
        super().__init__(
            init_query=[*init_query, page_operation],
        )


if __name__ == "__main__":
    print(ListQuery(name="listCase").select(name="observables")._data)
    lq: QueryExpr = (
        ListQuery(name="listCase")
        .filter(
            Gte(field="_createdAt", value=1234)
            & Eq(field="tags", value="edr")
            & Eq(field="source", value="edr")
        )
        .select("observables")
        .filter(Eq(field="dataType", value="ip"))
        .sort(Asc(field="_createdAt") & Desc(field="data"))
        .page(Paginate(start=0, end=10, extra_data=[]))
    )

    print(json.dumps(lq._data, indent=2, cls=_SessionJSONEncoder))

    gq = (
        GetQuery(name="getAlert", id_or_name="~1234")
        .select(name="observables")
        .select(name="tags")
    )
