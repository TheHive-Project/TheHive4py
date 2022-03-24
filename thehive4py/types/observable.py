from typing import List, TypedDict

from thehive4py.types.attachment import OutputAttachment


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
    attachment: str


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
    attachment: OutputAttachment
    tags: List[str]
    sightedAt: int
    message: str


class InputUpdateObservable(TypedDict, total=False):
    dataType: str
    message: str
    tlp: int
    pap: int
    tags: List[str]
    ioc: bool
    sighted: bool
    sightedAt: int
    ignoreSimilarity: bool


class InputBulkUpdateObservable(InputUpdateObservable):
    ids: List[str]
