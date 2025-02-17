from typing import Any, Dict, List, TypedDict


class OutputAnalyzerRequired(TypedDict):
    id: str
    name: str
    version: str
    description: str


class OutputAnalyzer(OutputAnalyzerRequired, total=False):
    dataTypeList: List[str]
    cortexIds: List[str]


class OutputResponderRequired(TypedDict):
    id: str
    name: str
    version: str
    description: str


class OutputResponder(OutputResponderRequired, total=False):
    dataTypeList: List[str]
    cortexIds: List[str]


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


class OutputAnalyzerJob(OutputAnalyzerJobRequired, total=False):
    _updatedBy: str
    _updatedAt: str
    endDate: str
    report: Dict[str, Any]
    case_artifact: Dict[str, Any]


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
    report: Dict[str, Any]
    responderName: str
    responderDefinition: str


class InputResponderActionRequired(TypedDict):
    objectId: str
    objectType: str
    responderId: str


class InputResponderAction(InputResponderActionRequired, total=False):
    parameters: Dict[str, Any]
    tlp: int


class InputAnalyzerJobRequired(TypedDict):
    analyzerId: str
    cortexId: str
    artifactId: str


class InputAnalyzerJob(InputAnalyzerJobRequired, total=False):
    parameters: Dict[str, Any]
