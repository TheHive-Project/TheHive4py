from typing import TypedDict


class InputCasePageRequired(TypedDict):
    title: str
    content: str
    category: str


class InputCasePage(InputCasePageRequired, total=False):
    order: int


class OutputCasePageRequired(TypedDict):
    _id: str
    id: str
    createdBy: str
    createdAt: int
    title: str
    content: str
    _type: str
    slug: str
    order: int
    category: str


class OutputCasePage(OutputCasePageRequired, total=False):
    updatedBy: str
    updatedAt: int


class InputUpdateCasePage(TypedDict, total=False):
    title: str
    content: str
    category: str
    order: int
