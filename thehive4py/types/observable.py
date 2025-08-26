from typing import List, TypedDict, Union

from typing_extensions import NotRequired

from thehive4py.types.attachment import InputAttachment, OutputAttachment


class InputObservable(TypedDict):
    dataType: str
    data: NotRequired[Union[str, List[str]]]
    message: NotRequired[str]
    startDate: NotRequired[int]
    attachment: NotRequired[
        Union[List[InputAttachment], List[str], InputAttachment, str]
    ]
    tlp: NotRequired[int]
    pap: NotRequired[int]
    tags: NotRequired[List[str]]
    ioc: NotRequired[bool]
    sighted: NotRequired[bool]
    sightedAt: NotRequired[int]
    ignoreSimilarity: NotRequired[bool]
    isZip: NotRequired[bool]
    zipPassword: NotRequired[str]


class OutputObservable(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    dataType: str
    data: NotRequired[str]
    startDate: int
    attachment: NotRequired[OutputAttachment]
    tlp: int
    tlpLabel: str
    pap: int
    papLabel: str
    tags: NotRequired[List[str]]
    ioc: bool
    sighted: bool
    sightedAt: NotRequired[int]
    reports: dict
    message: NotRequired[str]
    extraData: dict
    ignoreSimilarity: bool


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
