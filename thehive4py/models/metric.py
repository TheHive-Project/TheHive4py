from .model import Model


class Metric(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'name': None,
            'description': None,
        }

        if data is None:
            data = dict(defaults)

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}
