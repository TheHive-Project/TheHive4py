from .model import Model


class Task(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'description': None,
            'owner': None,
            'order': 0,
            'flag': False,
            'group': 'default',
            'startDate': None,
            'endDate': None
        }

        if data is None:
            data = dict(defaults)

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}


class TaskLog(Model):

    def __init__(self, data):
        defaults = {
            'message': None,
            'owner': None,
            'status': 'Ok',
            'startDate': None
        }

        if data is None:
            data = dict(defaults)

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}