from .model import Model


class Task(Model):

    def __init__(self, data):
        defaults = {
            'id': None,
            'status': None,
            'title': None,
            'owner': None,
            'order': 0,
            'flag': False,
            'group': 'default',
            'startDate': None,
            'endDate': None
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in data.items() if not k.startswith('_')}