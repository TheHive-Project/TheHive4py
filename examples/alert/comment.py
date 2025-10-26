import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

alert_to_comment = hive.alert.create(
    alert={
        "type": "comment-on-alert",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert with a comment",
        "description": "an alert to comment on",
    },
)

hive.comment.create_in_alert(
    alert_id=alert_to_comment["_id"],
    comment={"message": "what an average alert to comment on"},
)
