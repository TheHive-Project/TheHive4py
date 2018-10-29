import json
import os
import magic

from typing import List

from .abstract import AbstractController
from ..models import Observable
from ..query import *


class ObservablesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/artifact', api)

    def find_all(self, query, **kwargs) -> List[Observable]:
        return self._wrap(self._find_all(query, **kwargs), Observable)

    def find_one_by(self, query, **kwargs) -> Observable:
        return self._wrap(self._find_one_by(query, **kwargs), Observable)

    def get_by_id(self, org_id) -> Observable:
        return self._wrap(self._get_by_id(org_id), Observable)

    def of_case(self, case_id, query={}, **kwargs) -> List[Observable]:
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self.find_all(And(parent_expr, query), **kwargs)
        else:
            return self.find_all(parent_expr, **kwargs)

    def of_type(self, data_type, query={}, **kwargs) -> List[Observable]:
        type_expr = Eq('dataType', data_type)

        if query is not None and len(query) is not 0:
            return self.find_all(And(type_expr, query), **kwargs)
        else:
            return self.find_all(type_expr, **kwargs)

    def create(self, case_id, data) -> Observable:
        url = 'case/{}/artifact'.format(case_id)

        if isinstance(data, dict):
            data = Observable(data).json()
        elif isinstance(data, Observable):
            data = data.json()

        if data['dataType'] == 'file':
            post_data = {
                '_json': json.dumps({k: v for k, v in data.items() if not k == 'data'})
            }
            file_path = data['data']
            file_mime = magic.Magic(mime=True).from_file(file_path)

            file_def = {
                'attachment': (os.path.basename(file_path), open(file_path, 'rb'), file_mime)
            }

            return self._wrap(self._api.do_file_post(url, post_data, files=file_def), Observable)
        else:
            return self._wrap(self._api.do_post(url, data, {}), Observable)

    def run_analyzer(self):
        # TODO
        pass
