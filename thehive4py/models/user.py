from .model import Model


class User(Model):

    def __init__(self, data):
        defaults = {
            'id': None,
            'login': None,
            'name': None,
            'status': 'Ok',
            'roles': ['read']
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in data.items() if not k.startswith('_')}
