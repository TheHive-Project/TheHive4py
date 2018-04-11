from .abstract import AbstractController
from ..models import Case


class CasesController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, api)

    def find_all(self, query, **kwargs) -> list:
        return AbstractController.find_all(self, query or {}, kwargs.get('sort', None), kwargs.get('range', None))

    def find_one_by(self, query) -> Case:
        pass