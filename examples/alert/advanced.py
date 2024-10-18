from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

simple_alert = hive.alert.create(
    alert={
        "type": "simple",
        "source": "tutorial",
        "sourceRef": "should-be-unique",
        "title": "a simple alert",
        "description": "a bit too simple",
    }
)
