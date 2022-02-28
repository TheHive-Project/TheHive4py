from typing import List, TypedDict


class InputTaskLogRequired(TypedDict):
    message: str


class InputTaskLog(InputTaskLogRequired, total=False):
    startDate: int
    includeInTimeline: int


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
    attachments: List[dict]  # TODO: typehint
    includeInTimeline: int


class InputUpdateTaskLog(TypedDict, total=False):
    message: str
    includeInTimeline: int
