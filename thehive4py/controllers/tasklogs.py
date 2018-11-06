import os
import magic
import json

from typing import List

from .abstract import AbstractController
from ..models import Task, TaskLog
from ..query import *


class TaskLogsController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/task/log', api)

    def find_all(self, task_id, query, **kwargs) -> List[TaskLog]:
        url = 'case/task/log/_search'.format(task_id)

        parent_expr = ParentId('case_task', task_id)
        status_expr = Not(Eq('status', 'Deleted'))

        if query is not None and len(query) is not 0:
            q = And(parent_expr, status_expr, query)
        else:
            q = And(parent_expr, status_expr)

        params = dict((k, kwargs.get(k, None)) for k in ('sort', 'range'))
        return self._wrap(self._api.do_post(url, {'query': q}, params).json(), TaskLog)

    def find_one_by(self, task_id, query, **kwargs) -> TaskLog:
        url = 'case/task/log/_search'.format(task_id)

        parent_expr = ParentId('case_task', task_id)
        status_expr = Not(Eq('status', 'Deleted'))

        if query is not None and len(query) is not 0:
            q = And(parent_expr, status_expr, query)
        else:
            q = And(parent_expr, status_expr)

        params = {
            'range': '0-1'
        }
        if 'sort' in kwargs:
            params['sort'] = kwargs['sort']

        collection = self._api.do_post(url, {'query': q or {}}, params).json()

        if len(collection) > 0:
            return self._wrap(collection[0], TaskLog)
        else:
            return None

    def get_by_id(self, task_log_id) -> TaskLog:
        return self._wrap(self._get_by_id(task_log_id), TaskLog)

    def of_task(self, task_id, query={}, **kwargs) -> List[TaskLog]:
        parent_expr = ParentId('case_task', task_id)

        if query is not None and len(query) is not 0:
            return self.find_all(task_id, And(parent_expr, query), **kwargs)
        else:
            return self.find_all(task_id, parent_expr, **kwargs)

    def create(self, task_id, task_log) -> TaskLog:
        url = 'case/task/{}/log'.format(task_id)

        if isinstance(task_log, dict):
            data = TaskLog(task_log).json()
        elif isinstance(task_log, TaskLog):
            data = task_log.json()

        if 'file' in data:
            post_data = {
                '_json': json.dumps({'message': data['message']})
            }
            file_path = data['file']
            file_mime = magic.Magic(mime=True).from_file(file_path)

            file_def = {
                'attachment': (os.path.basename(file_path), open(file_path, 'rb'), file_mime)
            }

            return self._wrap(self._api.do_file_post(url, post_data, files=file_def).json(), TaskLog)
        else:
            return self._wrap(self._api.do_post(url, {'message': data['message']}, {}).json(), TaskLog)

    def remove(self, task_log_id) -> bool:
        return self._api.do_delete('case/task/log/{}'.format(task_log_id))

    def run_responder(self, cortex_id, task_log_id, responder_name) -> dict:
        url = 'connector/cortex/action'

        post_data = {
            'cortexId': cortex_id,
            'objectType': 'case_task_log',
            'objectId': task_log_id,
            'responderName': responder_name
        }
        return self._api.do_post(url, post_data, {}).json()
