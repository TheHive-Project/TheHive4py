from typing import Dict, TypedDict


class OutputEntityRequired(TypedDict):
    _type: str
    _id: str
    _createdAt: int
    _createdBy: str


class OutputEntity(OutputEntityRequired, total=False):
    _updatedAt: int
    _updatedBy: str


class OutputAuditRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    operation: str
    requestId: str
    summary: Dict[str, Dict[str, int]]


class OutputAudit(OutputAuditRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    attributeName: str
    oldValue: str
    newValue: str
    obj: OutputEntity
