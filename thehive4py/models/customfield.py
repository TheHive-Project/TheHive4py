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
