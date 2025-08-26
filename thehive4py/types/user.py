from typing import List, Literal, TypedDict

from typing_extensions import NotRequired

InputUserType = Literal["Normal", "Service"]


class InputUser(TypedDict):
    login: str
    name: str
    email: NotRequired[str]
    password: NotRequired[str]
    profile: str
    organisation: NotRequired[str]
    type: NotRequired[InputUserType]


class OrganisationLink(TypedDict):
    toOrganisation: str
    linkType: str
    otherLinkType: str
    avatar: NotRequired[str]


class OutputOrganisationProfile(TypedDict):
    organisationId: str
    organisation: str
    profile: str
    avatar: NotRequired[str]
    links: NotRequired[List[OrganisationLink]]


class OutputUser(TypedDict):
    _id: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    login: str
    name: str
    email: NotRequired[str]
    hasKey: bool
    hasPassword: bool
    hasMFA: bool
    locked: bool
    profile: str
    permissions: NotRequired[List[str]]
    organisation: str
    avatar: NotRequired[str]
    organisations: NotRequired[List[OutputOrganisationProfile]]
    type: str
    defaultOrganisation: NotRequired[str]
    extraData: dict


class InputUpdateUser(TypedDict, total=False):
    name: str
    organisation: str
    profile: str
    locked: bool
    avatar: str
    email: str
    defaultOrganisation: str
    type: InputUserType


class InputUserOrganisation(TypedDict):
    organisation: str
    profile: str
    default: NotRequired[bool]


class OutputUserOrganisation(TypedDict):
    organisation: str
    profile: str
    default: bool
