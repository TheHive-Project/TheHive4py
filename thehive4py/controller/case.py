from .abstract import AbstractController
from ..models import Case


class CaseController(AbstractController):
    def __init__(self):
        AbstractController.__init__(self)

    def find_all(self, query, sort, range) -> list:
        pass

    def find_one_by(self, query) -> Case:
        pass
