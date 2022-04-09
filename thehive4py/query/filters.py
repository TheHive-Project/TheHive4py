from collections import UserDict
from logging import Filter


class FilterExpr(UserDict):
    """Base class for filter expressions."""

    def __and__(self, other: "FilterExpr") -> "FilterExpr":
        if not isinstance(other, FilterExpr):
            self._raise_type_error("&", self, other)
        args = self.get("_and", [self]) + other.get("_and", [other])
        return FilterExpr(_and=args)

    def __or__(self, other: "FilterExpr") -> "FilterExpr":
        if not isinstance(other, FilterExpr):
            self._raise_type_error("|", self, other)
        args = self.get("_or", [self]) + other.get("_or", [other])
        return FilterExpr(_or=args)

    def __invert__(self) -> "FilterExpr":
        return FilterExpr(_not=self)

    def _raise_type_error(self, operand, first, second):
        raise TypeError(
            f"unsupported operand type(s) for {operand}: "
            f"{type(first)} and {type(second)}"
        )


class Eq(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_field=field, _value=value)


class Like(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_like={"_field": field, "_value": value})


class Match(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_match={"_field": field, "_value": value})


class StartsWith(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_startsWith={"_field": field, "_value": value})


class EndsWith(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_endsWith={"_field": field, "_value": value})


class Contains(FilterExpr):
    def __init__(self, field: str):
        super().__init__(_contains=field)


class Gt(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_gt={field: value})


class Gte(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_gte={field: value})


class Lt(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_lt={field: value})


class Lte(FilterExpr):
    def __init__(self, field: str, value):
        super().__init__(_lte={field: value})


class Between(FilterExpr):
    def __init__(self, field: str, start: int, end: int):
        super().__init__(_between={"_field": field, "_from": start, "_to": end})


class Before(FilterExpr):
    def __init__(self, field: str, end: int):
        super().__init__(_between={"_field": field, "_to": end})


class After(FilterExpr):
    def __init__(self, field: str, start: int):
        super().__init__(_between={"_field": field, "_from": start})