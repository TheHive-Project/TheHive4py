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

            return self._wrap(self._api.do_file_post(url, post_data, files=file_def).json(), Observable)
        else:
            return self._wrap(self._api.do_post(url, data, {}).json(), Observable)

    def update(self, observable_id, data, fields=None) -> Observable:
        url = 'case/artifact/{}'.format(observable_id)

        updatable_fields = [
            'message',
            'owner',
            'ioc',
            'sighted',
            'tags',
            'tlp'
        ]

        patch = AbstractController._clean_changes(data, updatable_fields, fields)
        return self._wrap(self._api.do_patch(url, patch).json(), Observable)

    def stats_by(self, query, field, top=10):
        return self._stats_by(query, field, top)

    def run_analyzer(self, cortex_id, observable_id, analyzer_id) -> dict:
        url = 'connector/cortex/job'

        post_data = {
            'cortexId': cortex_id,
            'artifactId': observable_id,
            'analyzerId': analyzer_id
        }
        return self._api.do_post(url, post_data, {}).json()

    def run_responder(self, cortex_id, observable_id, responder_name) -> dict:
        url = 'connector/cortex/action'

        post_data = {
            'cortexId': cortex_id,
            'objectType': 'case_artifact',
            'objectId': observable_id,
            'responderName': responder_name
        }
        return self._api.do_post(url, post_data, {}).json()
