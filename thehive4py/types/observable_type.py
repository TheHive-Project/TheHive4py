from typing import TypedDict

from typing_extensions import NotRequired


class InputObservableType(TypedDict):
    name: str
    isAttachment: NotRequired[bool]


class OutputObservableType(TypedDict):
    _id: str
    _type: str
    _updatedAt: NotRequired[int]
    _updatedBy: NotRequired[str]
    _createdAt: int
    _createdBy: str
    name: str
    isAttachment: bool
