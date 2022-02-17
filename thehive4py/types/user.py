from typing import Any, List, TypedDict

Avatar = Any  # TODO: find the most suitable type


class InputUserRequired(TypedDict):
    login: str
    name: str
    profile: str


class InputUser(InputUserRequired, total=False):
    password: str
    organisation: str
    avatar: Avatar


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
    permissions: List[str]
    organistaion: str
    organisations: List[OutputOrganisationProfile]


class OutputUser(OutputUserRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    avatar: str
