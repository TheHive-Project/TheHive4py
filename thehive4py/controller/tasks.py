from .abstract import AbstractController
from ..query import *


class TasksController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/task', api)

    def of_case(self, case_id, query={}, **kwargs):
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self.find_all(And(parent_expr, query), **kwargs)
        else:
            return self.find_all(parent_expr, **kwargs)

    def get_waiting(self, query={}, **kwargs):
        if query is not None and len(query) is not 0:
            return AbstractController.find_all(self, And({'status': 'WAITING'}, query), **kwargs)
        else:
            return AbstractController.find_all(self, {'status': 'WAITING'}, **kwargs)

    def get_by_user(self, user_id, query={}, **kwargs):
        if query is not None and len(query) is not 0:
            return AbstractController.find_all(self, And({'owner': user_id}, query), **kwargs)
        else:
            return AbstractController.find_all(self, {'owner': user_id}, **kwargs)

    def get_logs(self, query, **kwargs):
        # TODO
        pass

    def add_log(self, task_log):
        # TODO
        pass

    def flag(self, query, flag):
        # TODO
        pass

    def close(self, query):
        # TODO
        pass

    def open(self, query):
        # TODO
        pass

    def cancel(self, query):
        # TODO
        pass