from typing import List

from .abstract import AbstractController
from ..models import Task, TaskLog
from ..query import *


class TasksController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/task', api)

    def find_all(self, query, **kwargs) -> List[Task]:
        return self._wrap(self._find_all(query, **kwargs), Task)

    def find_one_by(self, query, **kwargs) -> Task:
        return self._wrap(self._find_one_by(query, **kwargs), Task)

    def get_by_id(self, org_id) -> Task:
        return self._wrap(self._get_by_id(org_id), Task)

    def of_case(self, case_id, query={}, **kwargs) -> List[Task]:
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self.find_all(And(parent_expr, query), **kwargs)
        else:
            return self.find_all(parent_expr, **kwargs)

    def get_waiting(self, query={}, **kwargs) -> List[Task]:
        if query is not None and len(query) is not 0:
            return self.find_all(And({'status': 'Waiting'}, query), **kwargs)
        else:
            return self.find_all({'status': 'Waiting'}, **kwargs)

    def get_by_user(self, user_id, query={}, **kwargs) -> List[Task]:
        if query is not None and len(query) is not 0:
            return self.find_all(And({'owner': user_id}, query), **kwargs)
        else:
            return self.find_all({'owner': user_id}, **kwargs)

    def create(self, case_id, data) -> Task:
        if isinstance(data, dict):
            data = Task(data).json()
        elif isinstance(data, Case):
            data = data.json()

        return Task(self._api.do_post('case/{}/task'.format(case_id), data).json())

    def update(self, task_id, data, fields=None) -> Task:
        url = 'case/task/{}'.format(task_id)

        updatable_fields = [
            'title',
            'description',
            'group',
            'startDate',
            'owner',
            'flag',
            'endDate',
            'order'
        ]
        patch = AbstractController._clean_changes(data, updatable_fields, fields)
        return self._wrap(self._api.do_patch(url, patch).json(), Task)

    def get_logs(self, task_id, query, **kwargs) -> List[TaskLog]:
        url = 'case/task/{}/log/_search'.format(task_id)

        parent_expr = ParentId('case_task', task_id)
        status_expr = Not(Eq('status', 'Deleted'))

        if query is not None and len(query) is not 0:
            q = And(parent_expr, status_expr, query)
        else:
            q = And(parent_expr, status_expr)

        params = dict((k, kwargs.get(k, None)) for k in ('sort', 'range'))
        return self._wrap(self._api.do_post(url, {'query': q}, params).json(), TaskLog)

    def add_log(self, task_id, task_log):
        # TODO
        pass

    def flag(self, task_id, flag):
        return self.update(task_id, {'flag': flag})

    def close(self, task_id):
        return self.update(task_id, {'status': 'Completed'})

    def start(self, task_id):
        return self.update(task_id, {'status': 'InProgress'})

    def assign(self, task_id, user_id):
        return self.update(task_id, {'owner': user_id})

    def cancel(self, task_id):
        return self.update(task_id, {'status': 'Cancel'})
