from .abstract import AbstractController


class UsersController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'users', api)
