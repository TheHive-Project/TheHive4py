import json
import mimetypes
import os
from typing import Optional

from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.session import TheHiveSession
from thehive4py.types.observable import InputObservable


class EndpointBase:
    def __init__(self, session: TheHiveSession):
        self._session = session

    def _fileinfo_from_filepath(self, filepath: str) -> tuple:
        filename = os.path.split(filepath)[1]
        mimetype = mimetypes.guess_type(filepath)
        filestream = open(filepath, "rb")

        return (filename, filestream, mimetype)

    def _build_observable_kwargs(
        self, observable: InputObservable, observable_path: Optional[str] = None
    ) -> dict:
        if observable_path:
            kwargs = {
                "data": {"_json": json.dumps(observable)},
                "files": {"attachment": self._fileinfo_from_filepath(observable_path)},
            }
        else:
            kwargs = {"json": observable}

        return kwargs

    def _build_subquery(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> QueryExpr:

        subquery: QueryExpr = []
        if filters:
            subquery = [*subquery, {"_name": "filter", **filters}]
        if sortby:
            subquery = [*subquery, {"_name": "sort", **sortby}]
        if paginate:
            subquery = [*subquery, {"_name": "page", **paginate}]

        return subquery
