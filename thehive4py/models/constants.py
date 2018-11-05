from enum import Enum


class Tlp(Enum):

    WHITE = 0
    GREEN = 1
    AMBER = 2
    RED = 3


class Pap(Enum):

    WHITE = 0
    GREEN = 1
    AMBER = 2
    RED = 3


class Severity(Enum):

    LOW = 1
    MEDIUM = 2
    HIGH = 3
