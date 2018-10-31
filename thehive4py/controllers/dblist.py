class DBListController(object):
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

    def _find_all(self):
        result = []
        data = self._api.do_get('list/{}'.format(self._endpoint)).json()
        for item in data.items():
            item[1]['id'] = item[0]
            result.append(item[1])

        return result

    def _get_by_id(self, item_id) -> dict:
        item_data = self._api.do_get('list/{}'.format(self._endpoint)).json()[item_id]
        item_data['id'] = item_id

        return item_data

    def _create(self, data) -> dict:
        url = 'list/{}'.format(self._endpoint)
        post_data = {'value': data}

        id = self._api.do_post(url, post_data).json()

        return self._get_by_id(id)

    def remove(self, item_id) -> bool:
        return self._api.do_delete('list/{}'.format(item_id))

    @staticmethod
    def _clean_changes(source, allowed, selected=[]):
        if selected is not None and len(selected) > 0:
            fields = list(set(allowed) & set(selected) & set(source.keys()))
        else:
            fields = list(set(allowed) & set(source.keys()))

        return dict((k, source.get(k, None)) for k in fields)