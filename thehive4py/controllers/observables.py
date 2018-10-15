from .abstract import AbstractController
from ..query import *


class ObservablesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/artifact', api)

    def of_case(self, case_id, query, **kwargs):
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self.find_all(And(parent_expr, query), **kwargs)
        else:
            return self.find_all(parent_expr, **kwargs)
