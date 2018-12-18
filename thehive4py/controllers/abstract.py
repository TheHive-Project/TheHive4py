class AbstractController(object):
    def __init__(self, endpoint, api):
        self._api = api
        self._endpoint = endpoint

    def _wrap(self, data, cls):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return list(map(lambda item: cls(item), data))
        else:
            return data

    def _find_all(self, query, **kwargs):
        url = '{}/_search'.format(self._endpoint)
        params = dict((k, kwargs.get(k, None)) for k in ('sort', 'range'))

        return self._api.do_post(url, {'query': query or {}}, params).json()

    def _find_one_by(self, query, **kwargs):
        url = '{}/_search'.format(self._endpoint)

        params = {
            'range': '0-1'
        }
        if 'sort' in kwargs:
            params['sort'] = kwargs['sort']

        collection = self._api.do_post(url, {'query': query or {}}, params).json()

        if len(collection) > 0:
            return collection[0]
        else:
            return None

    def count(self, query={}):
        url = '{}/_search'.format(self._endpoint)
        response = self._api.do_post(url, {'query': query or {}}, {'range': '0-1'})

        return response.headers.get('X-Total')

    def _get_by_id(self, obj_id):
        url = '{}/{}'.format(self._endpoint, obj_id)

        return self._api.do_get(url).json()

    def _stats_by(self, query, field, top):
        url = '{}/_stats'.format(self._endpoint)

        payload = {
            'query': query or {},
            'stats': [
                {
                    '_agg': 'field',
                    '_field': field,
                    '_select': [{
                        '_agg': 'count'
                    }],
                    '_order': '-_count',
                    '_size': top
                }
            ]
        }

        return self._api.do_post(url, payload, {}).json()

    @staticmethod
    def _clean_changes(source, allowed, selected=[]):
        if selected is not None and len(selected) > 0:
            fields = list(set(allowed) & set(selected) & set(source.keys()))
        else:
            fields = list(set(allowed) & set(source.keys()))

        return dict((k, source.get(k, None)) for k in fields)