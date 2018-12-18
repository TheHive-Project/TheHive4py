import os
import magic
import json

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
        elif isinstance(data, Task):
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

    def stats_by(self, query, field, top=10):
        return self._stats_by(query, field, top)

    def flag(self, task_id, flag) -> Task:
        return self.update(task_id, {'flag': flag})

    def close(self, task_id) -> Task:
        return self.update(task_id, {'status': 'Completed'})

    def start(self, task_id) -> Task:
        return self.update(task_id, {'status': 'InProgress'})

    def assign(self, task_id, user_id) -> Task:
        return self.update(task_id, {'owner': user_id})

    def remove(self, task_id) -> Task:
        return self.update(task_id, {'status': 'Cancel'})

    def get_logs(self, task_id, query, **kwargs) -> List[TaskLog]:
        return self._api.tasklogs.of_task(task_id, query=query, **kwargs)

    def add_log(self, task_id, task_log) -> TaskLog:
        return self._api.tasklogs.create(task_id, task_log)

    def run_responder(self, cortex_id, task_id, responder_name) -> dict:
        url = 'connector/cortex/action'

        post_data = {
            'cortexId': cortex_id,
            'objectType': 'case_task',
            'objectId': task_id,
            'responderName': responder_name
        }
        return self._api.do_post(url, post_data, {}).json()