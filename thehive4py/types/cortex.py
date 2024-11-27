# thehive4py/types/cortex.py
from typing import Any, TypedDict


class OutputAnalyzerRequired(TypedDict):
    id: str
    name: str
    version: str
    description: str


class OutputAnalyzer(OutputAnalyzerRequired, total=False):
    dataTypeList: list[str]
    cortexIds: list[str]


class OutputResponderRequired(TypedDict):
    id: str
    name: str
    version: str
    description: str


class OutputResponder(OutputResponderRequired, total=False):
    dataTypeList: list[str]
    cortexIds: list[str]


class OutputAnalyzerJobRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: str
    analyzerId: str
    analyzerName: str
    analyzerDefinition: str
    status: str
    startDate: str
    cortexId: str
    cortexJobId: str
    id: str
    operations: str


class OutputAnalyzerJob(TypedDict, total=False):
    _updatedBy: str
    _updatedAt: str
    endDate: str
    report: dict[str, Any]
    case_artifact: dict[str, Any]


class OutputResponderActionRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: str
    responderId: str
    status: str
    startDate: str
    cortexId: str
    cortexJobId: str
    id: str
    operations: str


class OutputResponderAction(OutputResponderActionRequired, total=False):
    _updatedBy: str
    _updatedAt: str
    endDate: str
    report: dict[str, Any]
    responderName: str
    responderDefinition: str
