from collections import UserDict


class Paginate(UserDict):
    def __init__(self, start: int, end: int, extra_data=[]):
        super().__init__({"from": start, "to": end, "extraData": extra_data})
