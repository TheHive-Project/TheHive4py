from typing import List

from .abstract import AbstractController
from ..models import Case, Task
from ..query import *


class CasesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case', api)

    def find_all(self, query, **kwargs) -> List[Case]:
        return self._wrap(self._find_all(query, **kwargs), Case)

    def find_one_by(self, query, **kwargs) -> Case:
        return self._wrap(self._find_one_by(query, **kwargs), Case)

    def get_by_id(self, org_id) -> Case:
        return self._wrap(self._get_by_id(org_id), Case)

    def get_by_number(self, number):
        return self._wrap(self._find_one_by(Eq('caseId', number)), Case)

    def get_tasks(self, case_id, query, **kwargs) -> List[Task]:
        return self._api.tasks.of_case(case_id, query=query, **kwargs)

    # TODO
    def get_observables(self, case_id, query, **kwargs):
        return self._api.observables.of_case(case_id, query, **kwargs)

    def links(self, case_id) -> List[Case]:
        return self._wrap(self._api.do_get('case/{}/links'.format(case_id)), Case)

    def has_observable(self, case_query, observable_query, **kwargs) -> List[Case]:
        child_expr = Child('case_artifact', observable_query or {})

        if case_query and len(case_query):
            criteria = And(case_query, child_expr)
        else:
            criteria = child_expr

        return self.find_all(criteria, **kwargs)

    def create(self, case):
        # TODO
        pass

    def update(self, case, changes):
        # TODO
        pass

    def add_task(self, task):
        # TODO
        pass

    def add_observable(self, observable):
        # TODO
        pass

    def flag(self, flag):
        # TODO
        pass

    def close(self, case_id):
        # TODO
        pass

    def open(self, case_id):
        # TODO
        pass

    def add_metric(self, case_id, metric, value):
        # TODO
        pass

    def remove_metric(self, case_id, metric):
        # TODO
        pass

    def add_customfield(self, case_id, customfield, value):
        # TODO
        pass

    def remove_customfield(self, case_id, customfield, value):
        # TODO
        pass