from typing import List, TypedDict


class InputUserRequired(TypedDict):
    login: str
    name: str
    profile: str


class InputUser(InputUserRequired, total=False):
    email: str
    password: str
    organisation: str
    type: str


class OutputOrganisationProfile(TypedDict):
    organisationId: str
    organisation: str
    profile: str


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


class InputUserOrganisationRequired(TypedDict):
    organisation: str
    profile: str


class InputUserOrganisation(InputUserOrganisationRequired, total=False):
    default: bool


class OutputUserOrganisation(TypedDict):
    organisation: str
    profile: str
    default: bool
