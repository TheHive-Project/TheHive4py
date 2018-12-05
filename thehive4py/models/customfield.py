from .model import Model


class CustomField(Model):

    def __init__(self, data):
        defaults = {
            'name': None,
            'description': None,
            'reference': None,
            'type': None,
            'options': [],
            'mandatory': False
        }

        if data is None:
            data = dict(defaults)

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}


class CustomFieldHelper(object):
    def __init__(self):
        self.fields = {}

    def __add_field(self, type, name, value):
        custom_field = dict()
        custom_field['order'] = len(self.fields)
        custom_field[type] = value
        self.fields[name] = custom_field

    def add_date(self, name, value):
        self.__add_field('date', name, value)
        return self

    def add_string(self, name, value):
        self.__add_field('string', name, value)
        return self

    def add_boolean(self, name, value):
        self.__add_field('boolean', name, value)
        return self

    def add_number(self, name, value):
        self.__add_field('number', name, value)
        return self

    def build(self):
        return self.fields
