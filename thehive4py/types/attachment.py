from typing import List, TypedDict

from typing_extensions import NotRequired


class InputAttachment(TypedDict):
    name: str
    contentType: str
    id: str


class OutputAttachment(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    name: str
    hashes: List[str]
    size: int
    contentType: str
    id: str
    path: str
    extraData: dict
