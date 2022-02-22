from typing import Any, List, TypedDict

Attachment = Any  # TODO: find the most suitable type


class InputObservableRequired(TypedDict):
    dataType: str


class InputObservable(InputObservableRequired, total=False):
    data: str
    message: str
    startDate: int
    tlp: int
    pap: int
    tags: List[str]
    ioc: bool
    sighted: bool
    sightedAt: int
    ignoreSimilarity: bool
    isZip: bool
    zipPassword: bool


class OutputObservableRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    dataType: str
    startDate: int
    tlp: int
    pap: int
    ioc: bool
    sighted: bool
    reports: dict
    extraData: dict
    ignoreSimilarity: bool


class OutputObservable(OutputObservableRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    data: str
    attachment: Attachment
    tags: List[str]
    sightedAt: int
    message: str
