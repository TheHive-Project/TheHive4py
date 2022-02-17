from collections import UserDict


class SortExpr(UserDict):
    """Base class for sort expressions."""

    def __and__(self, other: "SortExpr") -> "SortExpr":
        return self._concat_expressions("&", self, other)

    def __or__(self, other: "SortExpr") -> "SortExpr":
        return self._concat_expressions("|", self, other)

    def _concat_expressions(
        self, operand: str, expr1: "SortExpr", expr2: "SortExpr"
    ) -> "SortExpr":
        if not isinstance(expr1, SortExpr) or not isinstance(expr2, SortExpr):
            self._raise_type_error(operand, expr1, expr2)
        return SortExpr(_fields=[*expr1["_fields"], *expr2["_fields"]])

    def _raise_type_error(self, operand, first, second):
        raise TypeError(
            f"unsupported operand type(s) for {operand}: "
            f"{type(first)} and {type(second)}"
        )


class Asc(SortExpr):
    def __init__(self, field: str):
        super().__init__(_fields=[{field: "asc"}])


class Desc(SortExpr):
    def __init__(self, field: str):
        super().__init__(_fields=[{field: "desc"}])
