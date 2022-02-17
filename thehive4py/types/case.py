from typing import List, Literal, TypedDict

from thehive4py.types.custom_field import InputCustomFieldValue, OutputCustomFieldValue

CaseStatusValue = Literal["Open", "Resolved", "Duplicated"]


class CaseStatus:
    Open: CaseStatusValue = "Open"
    Resolved: CaseStatusValue = "Resolved"
    Duplicated: CaseStatusValue = "Duplicated"


ResolutionStatusValue = Literal[
    "Indeterminate", "FalsePositive", "TruePositive", "Other", "Duplicated"
]


class ResolutionStatus:
    Indeterminate: ResolutionStatusValue = "Indeterminate"
    FalsePositive: ResolutionStatusValue = "FalsePositive"
    TruePositive: ResolutionStatusValue = "TruePositive"
    Other: ResolutionStatusValue = "Other"
    Duplicated: ResolutionStatusValue = "Duplicated"


ImpactStatusValue = Literal["NotApplicable", "WithImpact", "NoImpact"]


class ImpactStatus:
    NotApplicable: ImpactStatusValue = "NotApplicable"
    WithImpact: ImpactStatusValue = "WithImpact"
    NoImpact: ImpactStatusValue = "NoImpact"


class InputCaseRequired(TypedDict):
    title: str
    description: str


class InputCase(InputCaseRequired, total=False):
    startDate: int
    endDate: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    status: CaseStatusValue
    summary: str
    user: str
    customFieldValues: List[InputCustomFieldValue]


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
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    status: CaseStatusValue
    extraData: dict


class OutputCase(OutputCaseRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    endDate: int
    summary: str
    impactStatus: ImpactStatusValue
    resolutionStatus: ResolutionStatusValue
    assignee: str
    customFields: List[OutputCustomFieldValue]
