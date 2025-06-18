from typing import List, TypedDict, Union

from thehive4py.types.attachment import InputAttachment, OutputAttachment


class InputObservableRequired(TypedDict):
    dataType: str


class InputObservable(InputObservableRequired, total=False):
    data: Union[str, List[str]]
    message: str
    startDate: int
    attachment: Union[List[InputAttachment], List[str], InputAttachment, str]
    tlp: int
    pap: int
    tags: List[str]
    ioc: bool
    sighted: bool
    sightedAt: int
    ignoreSimilarity: bool
    isZip: bool
    zipPassword: str


class OutputObservableRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    dataType: str
    startDate: int
    tlp: int
    tlpLabel: str
    pap: int
    papLabel: str
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
    addTags: List[str]
    removeTags: List[str]


class InputBulkUpdateObservable(InputUpdateObservable):
    ids: List[str]
