from typing import List, Union

from .filters import Between, Contains, Eq  # noqa
from .filters import FilterExpr as _FilterExpr  # noqa
from .filters import Gt, Gte, Like, Lt, Lte  # noqa
from .filters import Match, Before, After, StartsWith, EndsWith  # noqa
from .page import Paginate
from .sort import Asc, Desc  # noqa
from .sort import SortExpr as _SortExpr

QueryExpr = List[Union[_FilterExpr, _SortExpr, Paginate, dict]]
