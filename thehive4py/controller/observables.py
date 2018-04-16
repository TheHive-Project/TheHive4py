from .abstract import AbstractController


class ObservablesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/artifact', api)
