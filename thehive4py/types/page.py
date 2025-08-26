from typing import TypedDict

from typing_extensions import NotRequired


class InputCasePage(TypedDict):
    title: str
    content: str
    order: NotRequired[int]
    category: str


class OutputCasePage(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    title: str
    content: str
    order: int
    category: str
    extraData: dict


class InputUpdateCasePage(TypedDict, total=False):
    title: str
    content: str
    category: str
    order: int
