from urllib3 import Retry

from thehive4py import TheHiveApi

simple_retries = Retry(
    total=5,
    backoff_factor=0.5,
    allowed_methods=["GET"],
    status_forcelist=[500],
)

hive = TheHiveApi(
    url="http://localhost:9000",
    apikey="h1v3b33",
    max_retries=simple_retries,
)
