from typing import List, TypedDict


class InputTaskRequired(TypedDict):
    title: str


class InputTask(InputTaskRequired, total=False):
    group: str
    description: str
    status: str
    flag: bool
    startDate: int
    endDate: int
    order: int
    dueDate: int
    assignee: str


class OutputTaskRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    title: str
    group: str
    status: str
    flag: bool
    order: int
    extraData: dict


class OutputTask(OutputTaskRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    description: str
    startDate: int
    endDate: int
    assignee: str
    dueDate: int


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


class InputBulkUpdateTask(InputUpdateTask):
    ids: List[str]
