from typing import List, TypedDict

from typing_extensions import NotRequired


class InputProfile(TypedDict):
    name: str
    permissions: NotRequired[List[str]]


class OutputProfile(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    name: str
    permissions: NotRequired[List[str]]
    editable: bool
    forAdmin: bool
    forOrg: bool
    consumesLicense: bool


class InputUpdateProfile(TypedDict, total=False):
    name: str
    permissions: List[str]
