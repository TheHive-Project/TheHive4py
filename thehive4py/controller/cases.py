from .abstract import AbstractController
from ..models import Case
from ..query import *


class CasesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case', api)

    def get_by_number(self, number):
        return AbstractController.find_one_by(self, {'caseId': number}, {})

    def get_tasks(self, case_id, query, **kwargs):
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self._api.tasks.find_all(And(parent_expr, query), **kwargs)
        else:
            return self._api.tasks.find_all(parent_expr, **kwargs)

    def get_observables(self, case_id, query, **kwargs):
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self._api.observables.find_all(And(parent_expr, query), **kwargs)
        else:
            return self._api.observables.find_all(parent_expr, **kwargs)
