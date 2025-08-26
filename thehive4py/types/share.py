from typing import TypedDict

from typing_extensions import NotRequired


class OutputShare(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    caseId: str
    profileName: str
    organisationName: str
    owner: bool
    taskRule: str
    observableRule: str


class InputShare(TypedDict):
    organisation: str
    share: NotRequired[bool]
    profile: NotRequired[str]
    taskRule: NotRequired[str]
    observableRule: NotRequired[str]
