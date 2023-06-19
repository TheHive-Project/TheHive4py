from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.comment import InputComment, InputUpdateComment, OutputComment


class CommentEndpoint(EndpointBase):
    """
    Class representing TheHive's comment endpoint.

    Parameters:
        - EndpointBase: TheHive4py EndpointBase class
    """

    def create_in_alert(self, alert_id: str, comment: InputComment) -> OutputComment:
        """
        Creates a comment in the specified alert.

        Parameters:
            - alert_id (str): The ID of the alert.
            - comment (InputComment): An object containing the comment data.

        Returns:
            - OutputComment: An object containing the created comment data.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/comment", json=comment
        )

    def create_in_case(self, case_id: str, comment: InputComment) -> OutputComment:
        """
        Creates a comment in the specified case.

        Parameters:
            - case_id (str): The ID of the case.
            - comment (InputComment): An object containing the comment data.

        Returns:
            - OutputComment: An object containing the created comment data.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/comment", json=comment
        )

    def get(self, comment_id: str) -> OutputComment:
        """
        Gets the comment data for the specified comment.

        Parameters:
            - comment_id (str): The ID of the comment.

        Returns:
            - OutputComment: An object containing the comment data.
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

    def delete(self, comment_id: str) -> None:
        """
        Deletes the specified comment.

        Parameters:
            - comment_id (str): The ID of the comment.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/comment/{comment_id}"
        )

    def update(self, comment_id: str, fields: InputUpdateComment) -> None:
        """
        Updates the specified comment with the provided fields.

        Parameters:
            - comment_id (str): The ID of the comment.
            - fields (InputUpdateComment): An object containing the updated comment data.

        Returns:
                None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/comment/{comment_id}", json=fields
        )
