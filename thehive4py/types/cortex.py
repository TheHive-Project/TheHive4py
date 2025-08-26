from typing import Any, Dict, List, TypedDict

from typing_extensions import NotRequired


class OutputAnalyzer(TypedDict):
    id: str
    name: str
    version: str
    description: str
    dataTypeList: NotRequired[List[str]]
    cortexIds: NotRequired[List[str]]


class OutputResponder(TypedDict):
    id: str
    name: str
    version: str
    description: str
    dataTypeList: NotRequired[List[str]]
    cortexIds: NotRequired[List[str]]


class OutputAnalyzerJob(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: str
    _updatedAt: NotRequired[str]
    analyzerId: str
    analyzerName: str
    analyzerDefinition: str
    status: str
    startDate: str
    endDate: NotRequired[str]
    report: NotRequired[Dict[str, Any]]
    cortexId: str
    cortexJobId: str
    id: str
    case_artifact: NotRequired[Dict[str, Any]]
    operations: str


class OutputResponderAction(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: str
    _updatedAt: NotRequired[str]
    responderId: str
    responderName: NotRequired[str]
    responderDefinition: NotRequired[str]
    cortexId: NotRequired[str]
    cortexJobId: NotRequired[str]
    objectType: str
    objectId: str
    status: str
    startDate: str
    endDate: NotRequired[str]
    operations: str
    report: Dict[str, Any]


class InputResponderAction(TypedDict):
    responderId: str
    cortexId: NotRequired[str]
    objectType: str
    objectId: str
    parameters: NotRequired[Dict[str, Any]]
    tlp: NotRequired[int]


class InputAnalyzerJob(TypedDict):
    analyzerId: str
    cortexId: str
    artifactId: str
    parameters: NotRequired[Dict[str, Any]]
