from .abstract import AbstractController


class UsersController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'user', api)

    def lock(self, login):
        # TODO
        pass

    def unlock(self, login):
        # TODO
        pass

    def get_key(self, login):
        # TODO
        pass

    def create_key(self, login):
        # TODO
        pass

    def revoke_key(self, login):
        # TODO
        pass