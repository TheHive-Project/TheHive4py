from typing import Any, TypedDict


class InputCustomFieldValueRequired(TypedDict):
    name: str


class InputCustomFieldValue(InputCustomFieldValueRequired, total=False):
    value: Any
    order: int


class OutputCustomFieldValue(TypedDict):
    _id: str
    name: str
    description: str
    type: str
    value: Any
    order: int
