import uuid

from thehive4py import TheHiveApi
from thehive4py.query.filters import Eq

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

antivirus_alert = hive.alert.create(
    alert={
        "type": "find-multiple",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert to find",
        "description": "an alert to find with others",
        "tags": ["antivirus"],
    }
)

phishing_alert = hive.alert.create(
    alert={
        "type": "find-multiple",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert to find",
        "description": "an alert to find with others",
        "tags": ["phishing"],
    }
)


raw_filters = {
    "_or": [
        {"_eq": {"_field": "tags", "_value": "antivirus"}},
        {"_eq": {"_field": "tags", "_value": "phishing"}},
    ]
}
all_alerts_with_raw_filters = hive.alert.find(filters=raw_filters)

class_filters = Eq(field="tags", value="antivirus") | Eq(field="tags", value="phishing")
all_alerts_with_class_filters = hive.alert.find(filters=class_filters)
