from typing import List, TypedDict

from thehive4py.types.attachment import OutputAttachment


class InputTaskLogRequired(TypedDict):
    message: str


class InputTaskLog(InputTaskLogRequired, total=False):
    startDate: int
    includeInTimeline: int
    attachments: List[str]


class OutputTaskLogRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    message: str
    date: int
    owner: str
    extraData: dict


class OutputTaskLog(OutputTaskLogRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    attachments: List[OutputAttachment]
    includeInTimeline: int


class InputUpdateTaskLog(TypedDict, total=False):
    message: str
    includeInTimeline: int
