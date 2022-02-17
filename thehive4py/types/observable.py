from typing import Any, List, TypedDict

Attachment = Any  # TODO: find the most suitable type


class InputObservableRequired(TypedDict):
    dataType: str
    data: str


class InputObservable(InputObservableRequired, total=False):
    message: str
    startDate: int
    attachment: Attachment
    tlp: int
    tags: List[str]
    ioc: bool
    sighted: bool
    ignoreSimilarity: bool


class OutputObservableRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    dataType: str
    startDate: int
    tlp: int
    tags: List[str]
    ioc: bool
    sighted: bool
    reports: dict
    extraData: dict


class OutputObservable(OutputObservableRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    data: str
    attachment: Attachment
    message: str
    ignoreSimilarity: bool
