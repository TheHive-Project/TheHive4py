class AbstractController(object):
    def __init__(self):
        pass

    def find_all(self, query, sort, range):
        pass

    def find_one_by(self, query):
        pass

    def update_one_by_id(self, id, **attributes):
        pass

    def update_one_by_object(self, updated_obj, limit_attributes=None):
        pass
