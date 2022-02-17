
import pytest
from thehive4py.client import TheHiveApi

from tests.utils import Container, reinit_hive_container, spawn_hive_container


@pytest.fixture(scope="session")
def thehive_container():
    container = spawn_hive_container()
    yield container


@pytest.fixture(scope="function")
def thehive(thehive_container: Container):
    client = TheHiveApi(
        url=thehive_container.url, username="admin@test-org-1", password="admin"
    )
    reinit_hive_container(client)
    yield client
