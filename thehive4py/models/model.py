import json


class Model(object):
    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

    def json(self):
        return self.__dict__
