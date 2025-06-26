from typing import Any, List, Literal, TypedDict, Union

from typing_extensions import NotRequired

CustomFieldType = Literal["string", "integer", "float", "boolean", "date", "url"]


class InputCustomFieldValue(TypedDict):
    name: str
    value: Any
    order: NotRequired[int]


class OutputCustomFieldValue(TypedDict):
    _id: str
    name: str
    type: str
    value: Any
    order: int


class InputCustomField(TypedDict):
    name: str
    displayName: NotRequired[str]
    group: str
    description: str
    type: CustomFieldType
    mandatory: NotRequired[bool]
    options: NotRequired[List[Any]]


class OutputCustomField(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    name: str
    displayName: str
    group: str
    description: str
    type: CustomFieldType
    options: Union[List[int], List[float], List[str]]
    mandatory: bool
    extraData: dict


class InputUpdateCustomField(TypedDict, total=False):
    displayName: str
    group: str
    description: str
    type: str
    options: list
    mandatory: bool
