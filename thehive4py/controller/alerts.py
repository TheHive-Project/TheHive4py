from .abstract import AbstractController


class AlertsController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'alert', api)
