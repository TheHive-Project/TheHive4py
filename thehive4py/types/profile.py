from typing import List, Literal, TypedDict

from typing_extensions import NotRequired

ProfileType = Literal["Organisation", "Admin", "External"]


class InputProfile(TypedDict):
    type: NotRequired[ProfileType]
    name: str
    permissions: NotRequired[List[str]]


class OutputProfile(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    type: ProfileType
    name: str
    permissions: NotRequired[List[str]]
    editable: bool
    forAdmin: bool
    forOrg: bool
    forExternal: bool
    consumesLicense: bool


class InputUpdateProfile(TypedDict, total=False):
    name: str
    permissions: List[str]
