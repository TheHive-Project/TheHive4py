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

    def get_by_id(self, id) -> Case:
        return self._wrap(self._get_by_id(id), Case)

    def get_by_number(self, number) -> Case:
        return self._wrap(self._find_one_by(Eq('caseId', number)), Case)

    def links(self, case_id) -> List[Case]:
        return self._wrap(self._api.do_get('case/{}/links'.format(case_id)), Case)

    def has_observable(self, case_query, observable_query, **kwargs) -> List[Case]:
        child_expr = Child('case_artifact', observable_query or {})

        if case_query and len(case_query):
            criteria = And(case_query, child_expr)
        else:
            criteria = child_expr

        return self.find_all(criteria, **kwargs)

    def create(self, data) -> Case:
        if isinstance(data, dict):
            data = Case(data).json()
        elif isinstance(data, Case):
            data = data.json()

        return Case(self._api.do_post('case', data).json())

    def update(self, case_id, data, fields=None) -> Case:
        url = 'case/{}'.format(case_id)

        updatable_fields = [
            'title',
            'description',
            'severity',
            'startDate',
            'owner',
            'flag',
            'tlp',
            'tags',
            'resolutionStatus',
            'impactStatus',
            'summary',
            'endDate',
            'metrics',
            'customFields'
        ]
        patch = AbstractController._clean_changes(data, updatable_fields, fields)
        return self._wrap(self._api.do_patch(url, patch).json(), Case)

    def flag(self, case_id, flag) -> Case:
        return self.update(case_id, {'flag': flag})

    def open(self, case_id):
        return self.update(case_id, {'status': 'Open'})

    def close(self, case_id, summary, resolution_status, impact='NoImpact'):
        return self.update(case_id, {
            'status': 'Resolved',
            'summary': summary,
            'resolutionStatus': resolution_status,
            'impact': impact
        })

    def get_tasks(self, case_id, query, **kwargs) -> List[Task]:
        return self._api.tasks.of_case(case_id, query=query, **kwargs)

    def get_observables(self, case_id, query, **kwargs):
        return self._api.observables.of_case(case_id, query, **kwargs)

    def add_task(self, case_id, task) -> Task:
        return self._api.tasks.create(case_id, task)

    def add_observable(self, case_id, observable):
        return self._api.observables.create(case_id, observable)
