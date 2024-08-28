from thehive4py.client import TheHiveApi
from thehive4py.types.alert import OutputAlert


class TestQueryEndpoint:
    def test_simple_query(self, thehive: TheHiveApi, test_alert: OutputAlert):
        queried_alerts = thehive.query.run(
            query=[{"_name": "getAlert", "idOrName": test_alert["_id"]}],
        )

        assert [test_alert] == queried_alerts
