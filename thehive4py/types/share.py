from typing import TypedDict


class OutputShareRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    caseId: str
    profileName: str
    organisationName: str
    owner: bool
    taskRule: str
    observableRule: str


class OutputShare(OutputShareRequired, total=False):
    _updatedBy: str
    _updatedAt: int


class InputShareRequired(TypedDict):
    organisation: str


class InputShare(InputShareRequired, total=False):
    share: bool
    profile: str
    taskRule: str
    observableRule: str
