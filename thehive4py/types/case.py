from typing import Any, List, Literal, TypedDict, Union

from typing_extensions import NotRequired

from thehive4py.types.observable import OutputObservable
from thehive4py.types.page import InputCasePage
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


class InputCase(TypedDict):
    title: str
    description: str
    severity: NotRequired[int]
    startDate: NotRequired[int]
    endDate: NotRequired[int]
    tags: NotRequired[List[str]]
    flag: NotRequired[bool]
    tlp: NotRequired[int]
    pap: NotRequired[int]
    status: NotRequired[CaseStatusValue]
    summary: NotRequired[str]
    assignee: NotRequired[str]
    access: NotRequired[dict]
    customFields: NotRequired[Union[List[InputCustomFieldValue], dict]]
    caseTemplate: NotRequired[str]
    tasks: NotRequired[List[InputTask]]
    pages: NotRequired[List[InputCasePage]]
    sharingParameters: NotRequired[List[InputShare]]
    taskRule: NotRequired[str]
    observableRule: NotRequired[str]


class OutputCase(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    number: int
    title: str
    description: str
    severity: int
    severityLabel: str
    startDate: int
    endDate: NotRequired[int]
    tags: NotRequired[List[str]]
    flag: bool
    tlp: int
    tlpLabel: str
    pap: int
    papLabel: str
    status: CaseStatusValue
    stage: str
    summary: NotRequired[str]
    impactStatus: NotRequired[ImpactStatusValue]
    assignee: NotRequired[str]
    access: dict
    customFields: NotRequired[List[OutputCustomFieldValue]]
    userPermissions: NotRequired[List[str]]
    extraData: dict
    newDate: int
    inProgressDate: NotRequired[int]
    closedDate: NotRequired[int]
    alertDate: NotRequired[int]
    alertNewDate: NotRequired[int]
    alertInProgressDate: NotRequired[int]
    alertImportedDate: NotRequired[int]
    timeToDetect: int
    timeToTriage: NotRequired[int]
    timeToQualify: NotRequired[int]
    timeToAcknowledge: NotRequired[int]
    timeToResolve: NotRequired[int]
    handlingDuration: NotRequired[int]


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
    customFields: Union[List[InputCustomFieldValue], dict]
    taskRule: str
    observableRule: str
    addTags: List[str]
    removeTags: List[str]


class InputBulkUpdateCase(InputUpdateCase):
    ids: List[str]


class InputImportCase(TypedDict):
    password: str
    sharingParameters: NotRequired[List[InputShare]]
    taskRule: NotRequired[str]
    observableRule: NotRequired[str]


class InputApplyCaseTemplate(TypedDict):
    ids: List[str]
    caseTemplate: str
    updateTitlePrefix: NotRequired[bool]
    updateDescription: NotRequired[bool]
    updateTags: NotRequired[bool]
    updateSeverity: NotRequired[bool]
    updateFlag: NotRequired[bool]
    updateTlp: NotRequired[bool]
    updatePap: NotRequired[bool]
    updateCustomFields: NotRequired[bool]
    importTasks: NotRequired[List[str]]
    importPages: NotRequired[List[str]]


class OutputCaseObservableMerge(TypedDict):
    untouched: int
    updated: int
    deleted: int


class OutputCaseLink(OutputCase):
    linksCount: int
    linkedWith: NotRequired[List[OutputObservable]]


class OutputImportCase(TypedDict):
    case: OutputCase
    observables: NotRequired[List[OutputObservable]]
    procedures: NotRequired[List[OutputObservable]]
    errors: NotRequired[List[Any]]


class InputCaseOwnerOrganisation(TypedDict):
    organisation: str
    keepProfile: NotRequired[str]
    taskRule: NotRequired[str]
    observableRule: NotRequired[str]


class InputCaseAccess(TypedDict):
    access: dict  # TODO: refine type hint


class InputCaseLink(TypedDict):
    type: str
    caseId: str


class InputURLLink(TypedDict):
    type: str
    url: str
