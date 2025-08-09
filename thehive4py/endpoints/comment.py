from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.comment import InputComment, InputUpdateComment, OutputComment


class CommentEndpoint(EndpointBase):
    def create_in_case(self, case_id: str, comment: InputComment) -> OutputComment:
        """Create a comment in a case.

        Args:
            case_id: The id of the case to add the comment to.
            comment: The body of the comment

        Returns:
            The created comment.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/comment", json=comment
        )

    def create_in_alert(self, alert_id: str, comment: InputComment) -> OutputComment:
        """Create a comment in an alert.

        Args:
            alert_id: The id of the alert to add the comment to.
            comment: The body of the comment.

        Returns:
            The created comment.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/comment", json=comment
        )

    def delete(self, comment_id: str) -> None:
        """Delete a comment.

        Args:
            comment_id: The id of the comment to delete.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/comment/{comment_id}"
        )

    def update(self, comment_id: str, fields: InputUpdateComment) -> None:
        """Update a comment.

        Args:
            comment_id: The id of the comment to update.
            fields: The fields to update in the comment.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/comment/{comment_id}", json=fields
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputComment]:
        """Find multiple comments.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of comments matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listComment"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": query},
            params={"name": "listComment"},
        )

    def get(self, comment_id: str) -> OutputComment:
        """Get a comment by id.

        Args:
            comment_id: The id of the comment.

        Returns:
            The comment specified by the id.
        """
        # TODO: temp implementation until a dedicated get endpoint
        comments = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": [{"_name": "getComment", "idOrName": comment_id}]},
        )
        try:
            return comments[0]
        except IndexError:
            raise TheHiveError("404 - Comment not found")
