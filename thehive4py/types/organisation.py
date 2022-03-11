from typing import List, TypedDict


class InputOrganisationLink(TypedDict, total=False):
    linkType: str
    otherLinkType: str


class InputBulkOrganisationLink(TypedDict):
    toOrganisation: str
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


class InputOrganisationRequired(TypedDict):
    name: str
    description: str


class InputOrganisation(InputOrganisationRequired, total=False):
    taskRule: str
    observableRule: str
    locked: bool


class OutputOrganisationRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    description: str
    taskRule: str
    observableRule: str
    locked: bool
    extraData: dict


class OutputOrganisation(OutputOrganisationRequired, total=False):

    _updatedBy: str
    _updatedAt: int
    links: List[InputOrganisationLink]
    avatar: str


class InputUpdateOrganisation(TypedDict, total=False):
    name: str
    description: str
    taskRule: str
    observableRule: str
    locked: bool
    avatar: str
