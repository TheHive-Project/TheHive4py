from .abstract import AbstractController
from ..models import Case
from ..query import *


class CasesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case', api)

    def get_by_number(self, number):
        return AbstractController.find_one_by(self, {'caseId': number}, {})

    def get_tasks(self, case_id, query, **kwargs):
        return self._api.tasks.of_case(case_id, query, **kwargs)

    def get_observables(self, case_id, query, **kwargs):
        return self._api.observables.of_case(case_id, query, **kwargs)

    def links(self, case_id):
        return self._api.do_get('case/{}/links'.format(case_id))

    def has_observable(self, case_query, observable_query, **kwargs):
        child_expr = Child('case_artifact', observable_query or {})

        if case_query and len(case_query):
            criteria = And(case_query, child_expr)
        else:
            criteria = child_expr

        return self.find_all(criteria, **kwargs)
