from typing import List, TypedDict

from typing_extensions import NotRequired

from thehive4py.types.attachment import OutputAttachment


class InputTaskLog(TypedDict):
    message: str
    startDate: NotRequired[int]
    includeInTimeline: NotRequired[int]
    attachments: NotRequired[List[str]]


class OutputTaskLog(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    message: str
    date: int
    attachments: NotRequired[List[OutputAttachment]]
    owner: str
    includeInTimeline: NotRequired[int]
    extraData: dict


class InputUpdateTaskLog(TypedDict, total=False):
    message: str
    includeInTimeline: int
