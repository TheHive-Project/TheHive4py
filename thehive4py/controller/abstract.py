class AbstractController(object):
    def __init__(self, endpoint, api):
        self._api = api
        self._endpoint = endpoint

    def find_all(self, query, **kwargs):
        url = '{}/_search'.format(self._endpoint)
        params = dict((k, kwargs.get(k, None)) for k in ('sort', 'range'))

        return self._api.do_post(url, {'query': query or {}}, params)

    def find_one_by(self, query, kwargs):
        url = '{}/_search'.format(self._endpoint)

        params = {
            'range': '0-1'
        }
        if 'sort' in kwargs:
            params['sort'] = kwargs['sort']

        return self._api.do_post(url, {'query': query or {}}, params)

    def count(self, query):
        url = '{}/_stats'.format(self._endpoint)

        payload = {
            'query': query or {},
            'stats': [{
                '_agg': 'count'
            }]
        }

        return self._api.do_post(url, payload, {})['count']

    def get_by_id(self, id):
        url = '{}/{}'.format(self._endpoint, id)

        return self._api.do_get(url)

    def update_one_by_id(self, id, **attributes):
        pass

    def update_one_by_object(self, updated_obj, limit_attributes=None):
        pass
