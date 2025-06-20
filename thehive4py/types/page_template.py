from typing import TypedDict

from typing_extensions import Required


class InputPageTemplate(TypedDict, total=False):
    title: Required[str]
    content: Required[str]
    order: int
    category: Required[str]


class OutputPageTemplate(TypedDict, total=False):
    _id: Required[str]
    _type: Required[str]
    _createdBy: Required[str]
    _updatedBy: str
    _createdAt: Required[int]
    _updatedAt: int
    title: Required[str]
    content: Required[str]
    order: Required[int]
    category: Required[str]
    extraData: Required[dict]


class InputUpdatePageTemplate(TypedDict, total=False):
    title: str
    content: str
    order: int
    category: str
