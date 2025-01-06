from collections import UserDict as _UserDict
from typing import Any as _Any
from typing import Union as _Union
import warnings

FilterExpr = _Union["_FilterBase", dict]


class _FilterBase(_UserDict):
    """Base class for filters."""

    def __and__(self, other: "_FilterBase") -> "_FilterBase":
        if not isinstance(other, _FilterBase):
            self._raise_type_error("&", self, other)
        args = self.get("_and", [self]) + other.get("_and", [other])
        return _FilterBase(_and=args)

    def __or__(self, other: "_FilterBase") -> "_FilterBase":  # type:ignore
        if not isinstance(other, _FilterBase):
            self._raise_type_error("|", self, other)
        args = self.get("_or", [self]) + other.get("_or", [other])
        return _FilterBase(_or=args)

    def __invert__(self) -> "_FilterBase":
        return _FilterBase(_not=self)

    def _raise_type_error(self, operand, first, second):
        raise TypeError(
            f"unsupported operand type(s) for {operand}: "
            f"{type(first)} and {type(second)}"
        )


class Lt(_FilterBase):
    """Field less than value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_lt={"_field": field, "_value": value})


class Gt(_FilterBase):
    """Field greater than value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_gt={"_field": field, "_value": value})


class Lte(_FilterBase):
    """Field less than or equal value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_lte={"_field": field, "_value": value})


class Gte(_FilterBase):
    """Field less than or equal value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_gte={"_field": field, "_value": value})


class Ne(_FilterBase):
    """Field not equal value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_ne={"_field": field, "_value": value})


class Eq(_FilterBase):
    """Field equal value."""

    def __init__(self, field: str, value: _Any):
        super().__init__(_eq={"_field": field, "_value": value})


class StartsWith(_FilterBase):
    """Field starts with value."""

    def __init__(self, field: str, value: str):
        super().__init__(_startsWith={"_field": field, "_value": value})


class EndsWith(_FilterBase):
    """Field ends with value."""

    def __init__(self, field: str, value: str):
        super().__init__(_endsWith={"_field": field, "_value": value})


class Id(_FilterBase):
    """FIlter by ID."""

    def __init__(self, id: str):
        super().__init__(_id=id)


class Between(_FilterBase):
    """Field between inclusive from and exclusive to values."""

    def __init__(self, field: str, start: int, end: int):
        super().__init__(_between={"_field": field, "_from": start, "_to": end})


class In(_FilterBase):
    """Field is one of the values."""

    def __init__(self, field: _Any, values: list):
        super().__init__(_in={"_field": field, "_values": values})


class Contains(_FilterBase):
    """Object contains the field."""

    def __init__(self, field: str):
        warnings.warn(
            message="The `Contains` filter has been deprecated. "
            "Please use the `Has` filter to prevent breaking "
            "changes in the future.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(_contains=field)


class Has(_FilterBase):
    """Object contains the field."""

    def __init__(self, field: str):
        super().__init__(_has=field)


class Like(_FilterBase):
    """Field contains the value."""

    def __init__(self, field: str, value: str):
        super().__init__(_like={"_field": field, "_value": value})


class Match(_FilterBase):
    """Field contains the value"""

    def __init__(self, field: str, value: str):
        super().__init__(_match={"_field": field, "_value": value})
