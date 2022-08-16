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


class InputCustomFieldRequired(TypedDict):
    name: str
    group: str
    description: str
    type: str


class InputCustomField(InputCustomFieldRequired, total=False):
    displayName: str
    mandatory: bool
    options: list


class OutputCustomFieldRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    displayName: str
    group: str
    description: str
    type: str
    mandatory: bool


class OutputCustomField(OutputCustomFieldRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    options: list


class InputUpdateCustomField(TypedDict, total=False):
    displayName: str
    group: str
    description: str
    type: str
    options: list
    mandatory: bool
