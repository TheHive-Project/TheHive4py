from typing import List, Literal, TypedDict

from thehive4py.types.share import InputShare

from .custom_field import InputCustomFieldValue, OutputCustomFieldValue
from .task import InputTask

CaseStatusValue = Literal[
    "New",
    "InProgress",
    "Indeterminate",
    "FalsePositive",
    "TruePositive",
    "Other",
    "Duplicated",
]


class CaseStatus:
    New: CaseStatusValue = "New"
    InProgress: CaseStatusValue = "InProgress"
    Indeterminate: CaseStatusValue = "Indeterminate"
    FalsePositive: CaseStatusValue = "FalsePositive"
    TruePositive: CaseStatusValue = "TruePositive"
    Other: CaseStatusValue = "Other"
    Duplicated: CaseStatusValue = "Duplicated"


ImpactStatusValue = Literal["NotApplicable", "WithImpact", "NoImpact"]


class ImpactStatus:
    NotApplicable: ImpactStatusValue = "NotApplicable"
    WithImpact: ImpactStatusValue = "WithImpact"
    NoImpact: ImpactStatusValue = "NoImpact"


class InputCaseRequired(TypedDict):
    title: str
    description: str


class InputCase(InputCaseRequired, total=False):
    severity: int
    startDate: int
    endDate: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    status: CaseStatusValue
    summary: str
    assignee: str
    customFields: List[InputCustomFieldValue]
    caseTemplate: str
    tasks: List[InputTask]
    sharingParameters: List[InputShare]
    taskRule: str
    observableRule: str


class OutputCaseRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    number: int
    title: str
    description: str
    severity: int
    startDate: int
    flag: bool
    tlp: int
    pap: int
    status: CaseStatusValue
    stage: str
    extraData: dict
    newDate: int
    timeToDetect: int


class OutputCase(OutputCaseRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    endDate: int
    tags: List[str]
    summary: str
    impactStatus: ImpactStatusValue
    assignee: str
    customFields: List[OutputCustomFieldValue]
    userPermissions: List[str]
    inProgressDate: int
    closedDate: int
    alertDate: int
    alertNewDate: int
    alertInProgressDate: int
    alertImportedDate: int
    timeToTriage: int
    timeToQualify: int
    timeToAcknowledge: int
    timeToResolve: int
    handlingDuration: int


class InputUpdateCase(TypedDict, total=False):
    title: str
    description: str
    severity: int
    startDate: int
    endDate: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    status: str
    summary: str
    assignee: str
    impactStatus: str
    customFields: List[InputCustomFieldValue]
    taskRule: str
    observableRule: str


class InputBulkUpdateCase(InputUpdateCase):
    ids: List[str]


class InputImportCaseRequired(TypedDict):
    password: str


class InputImportCase(InputImportCaseRequired, total=False):
    sharingParameters: List[InputShare]
    taskRule: str
    observableRule: str
