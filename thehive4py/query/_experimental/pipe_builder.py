from collections import UserList
from encodings.punycode import selective_find
from typing import Any, Iterable, TypeVar, Union, overload

from typing_extensions import Self

"""
QueryExpr
FilteredQueryExpr
SortedQueryExpr
PagedQueryExpr
"""

Query = Union["QueryExpr"]

QueryExpr = Union[
    "_SelectedQueryExpr",
    "_FilteredQueryExpr",
    "_SortedQueryExpr",
]

TQueryExpr = TypeVar(
    "TQueryExpr",
    "_SelectedQueryExpr",
    "_FilteredQueryExpr",
    "_SortedQueryExpr",
    "_PagedQueryExpr",
)
TPreSortQueryExpr = TypeVar(
    "TPreSortQueryExpr",
    "_SelectedQueryExpr",
    "_FilteredQueryExpr",
)


class _QueryExprBase(UserList):
    def __radd__(self, other: "_QueryExprBase"):
        return NotImplemented


class _SelectedQueryExpr(_QueryExprBase):
    def __add__(
        self,
        query_expr: TQueryExpr,
    ) -> TQueryExpr:
        return query_expr.__class__(initlist=self + query_expr)

    def __radd__(
        self,
        query_expr: TQueryExpr,
    ) -> "_SelectedQueryExpr":
        return _SelectedQueryExpr(initlist=query_expr + self)


class _FilteredQueryExpr(_QueryExprBase):
    def __add__(
        self,
        query_expr: TQueryExpr,
    ) -> TQueryExpr:
        return query_expr.__class__(initlist=self + query_expr)

    def __radd__(
        self,
        query_expr: _SelectedQueryExpr,
    ) -> "_FilteredQueryExpr":
        return _FilteredQueryExpr(initlist=query_expr + self)


class _SortedQueryExpr(_QueryExprBase):
    def __add__(self, query_expr: "_PagedQueryExpr"):
        return _PagedQueryExpr(initlist=query_expr + self)

    def __radd__(self, query_expr: TPreSortQueryExpr) -> "_SortedQueryExpr":
        return _SortedQueryExpr(initlist=query_expr + self)


class _PagedQueryExpr(_QueryExprBase):
    def __add__(self, query_expr):
        return NotImplemented


def Select(name: str) -> _SelectedQueryExpr:
    query_selector = {"_name": name}
    return _SelectedQueryExpr(initlist=[query_selector])


def Filter(filter_expr: dict) -> _FilteredQueryExpr:
    query_filter = {"_name": "filter", **filter_expr}
    return _FilteredQueryExpr(initlist=[query_filter])


def Sort(sort_expr: dict) -> _SortedQueryExpr:
    query_sorter = {"_name": "sort", **sort_expr}
    return _SortedQueryExpr(initlist=[query_sorter])


def Page(page_expr: dict) -> _PagedQueryExpr:
    query_page = {"_name": "page", **page_expr}
    return _PagedQueryExpr(initlist=[query_page])


q = (
    Select("listCase")
    + Filter({})
    + Sort({})
    + Select("")
    + Select("")
    + Sort({})
    + Page({})
)
