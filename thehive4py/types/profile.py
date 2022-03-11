from typing import List, TypedDict


class InputProfileRequired(TypedDict):
    name: str


class InputProfile(InputProfileRequired, total=False):
    permissions: List[str]


class OutputProfileRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    editable: bool
    isAdmin: bool


class OutputProfile(OutputProfileRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    permissions: List[str]


class InputUpdateProfile(TypedDict, total=False):
    name: str
    permissions: List[str]
