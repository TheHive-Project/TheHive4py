from typing import List, TypedDict, Union

from thehive4py.types.custom_field import InputCustomFieldValue
from thehive4py.types.page import InputCasePage
from thehive4py.types.share import InputShare
from thehive4py.types.task import InputTask


class OutputMISPStatus(TypedDict):
    status: dict
    syncInProgress: bool


class InputMISPImportCase(TypedDict, total=False):
    caseTemplate: str
    assignee: str
    tasks: List[InputTask]
    pages: List[InputCasePage]
    customFields: Union[dict, List[InputCustomFieldValue]]
    sharingParameters: List[InputShare]
    taskRule: str
    observableRule: str
