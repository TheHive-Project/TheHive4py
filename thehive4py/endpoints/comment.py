from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.comment import InputComment, InputUpdateComment, OutputComment


class CommentEndpoint(EndpointBase):
    def create_in_alert(self, alert_id: str, comment: InputComment) -> OutputComment:
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/comment", json=comment
        )

    def create_in_case(self, case_id: str, comment: InputComment) -> OutputComment:
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/comment", json=comment
        )

    def get(self, comment_id: str) -> OutputComment:
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
        return self._session.make_request(
            "DELETE", path=f"/api/v1/comment/{comment_id}"
        )

    def update(self, comment_id: str, fields: InputUpdateComment) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/comment/{comment_id}", json=fields
        )
