from typing import List, TypedDict

from typing_extensions import NotRequired


class InputOrganisationLink(TypedDict, total=False):
    linkType: str
    otherLinkType: str


class InputBulkOrganisationLink(TypedDict):
    toOrganisation: str
    avatar: NotRequired[str]
    linkType: str
    otherLinkType: str


class OutputSharingProfile(TypedDict):
    name: str
    description: str
    autoShare: bool
    editable: bool
    permissionProfile: str
    taskRule: str
    observableRule: str


class InputOrganisation(TypedDict):
    name: str
    description: str
    taskRule: NotRequired[str]
    observableRule: NotRequired[str]
    locked: NotRequired[bool]


class OutputOrganisation(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    name: str
    description: str
    taskRule: str
    observableRule: str
    links: NotRequired[List[InputOrganisationLink]]
    avatar: NotRequired[str]
    locked: bool
    extraData: dict


class InputUpdateOrganisation(TypedDict, total=False):
    name: str
    description: str
    taskRule: str
    observableRule: str
    locked: bool
    avatar: str


class OutputOrganisationLink(TypedDict):
    linkType: str
    otherLinkType: str
    organisation: OutputOrganisation
