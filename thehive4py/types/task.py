from typing import List, TypedDict

from typing_extensions import NotRequired


class InputTask(TypedDict):
    title: str
    group: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[str]
    flag: NotRequired[bool]
    startDate: NotRequired[int]
    endDate: NotRequired[int]
    order: NotRequired[int]
    dueDate: NotRequired[int]
    assignee: NotRequired[str]
    mandatory: NotRequired[bool]


class OutputTask(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    title: str
    group: str
    description: NotRequired[str]
    status: str
    flag: bool
    startDate: NotRequired[int]
    endDate: NotRequired[int]
    assignee: NotRequired[str]
    order: int
    dueDate: NotRequired[int]
    mandatory: bool
    extraData: dict


class InputUpdateTask(TypedDict, total=False):
    title: str
    group: str
    description: str
    status: str
    flag: bool
    startDate: int
    endDate: int
    order: int
    dueDate: int
    assignee: str
    mandatory: bool


class InputBulkUpdateTask(InputUpdateTask):
    ids: List[str]
