from typing import List, Union

from .filters import Between, Contains, EndsWith, Eq
from .filters import FilterExpr as _FilterExpr
from .filters import Gt, Gte, Has, Id, In, Like, Lt, Lte, Match, Ne, StartsWith
from .page import Paginate
from .sort import Asc, Desc
from .sort import SortExpr as _SortExpr

QueryExpr = List[Union[_FilterExpr, _SortExpr, Paginate, dict]]
