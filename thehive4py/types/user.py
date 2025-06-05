from typing import List, Literal, TypedDict

InputUserType = Literal["Normal", "Service"]


class InputUserRequired(TypedDict):
    login: str
    name: str
    profile: str


class InputUser(InputUserRequired, total=False):
    email: str
    password: str
    organisation: str
    type: InputUserType


class OrganisationLinkRequired(TypedDict):
    toOrganisation: str
    linkType: str
    otherLinkType: str


class OrganisationLink(OrganisationLinkRequired, total=False):
    avatar: str


class OutputOrganisationProfileRequired(TypedDict):
    organisationId: str
    organisation: str
    profile: str


class OutputOrganisationProfile(OutputOrganisationProfileRequired, total=False):
    avatar: str
    links: List[OrganisationLink]


class OutputUserRequired(TypedDict):
    _id: str
    _createdBy: str
    _createdAt: int
    login: str
    name: str
    hasKey: bool
    hasPassword: bool
    hasMFA: bool
    locked: bool
    profile: str
    organisation: str
    type: str
    extraData: dict


class OutputUser(OutputUserRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    email: str
    permissions: List[str]
    avatar: str
    organisations: List[OutputOrganisationProfile]
    defaultOrganisation: str


class InputUpdateUser(TypedDict, total=False):
    name: str
    organisation: str
    profile: str
    locked: bool
    avatar: str
    email: str
    defaultOrganisation: str
    type: InputUserType


class InputUserOrganisationRequired(TypedDict):
    organisation: str
    profile: str


class InputUserOrganisation(InputUserOrganisationRequired, total=False):
    default: bool


class OutputUserOrganisation(TypedDict):
    organisation: str
    profile: str
    default: bool
