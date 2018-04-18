from .abstract import AbstractController


class AlertsController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'alert', api)

    def import_as_case(self, alert_id, template=None):
        # TODO
        pass

    def merge_into(self, alert_id, case_id):
        # TODO
        pass