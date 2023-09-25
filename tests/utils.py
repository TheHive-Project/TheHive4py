import shlex
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

import requests

from thehive4py.client import TheHiveApi
from thehive4py.query.filters import Eq


@dataclass
class TestConfig:
    __test__ = False

    image_name: str
    container_name: str

    user: str
    password: str

    admin_org: str
    main_org: str
    share_org: str


def _is_container_responsive(container_url: str) -> bool:
    COOLDOWN = 1.0
    TIMEOUT = 60.0

    now = time.time()
    end = now + TIMEOUT

    while now < end:
        try:
            response = requests.get(f"{container_url}/api/status")
            if response.ok:
                return True
        except Exception:
            pass

        time.sleep(COOLDOWN)
        now = time.time()
    return False


def _is_container_exist(container_name: str) -> bool:
    exist_cmd = subprocess.run(
        shlex.split(f"docker ps -aq --filter name={container_name}"),
        capture_output=True,
        text=True,
    )
    return bool(exist_cmd.stdout.strip())


def _get_container_port(container_name: str) -> str:
    port_cmd = subprocess.run(
        shlex.split(f"docker port {container_name}"), capture_output=True, text=True
    )
    port = port_cmd.stdout.strip().split(":")[-1]
    return port


def _build_container_url(container_name: str) -> str:
    port = _get_container_port(container_name)
    return f"http://localhost:{port}"


def _run_container(container_name: str, container_image: str):
    subprocess.run(
        shlex.split(
            f"docker run -d --rm -p 9000 --name {container_name} {container_image}"
        ),
        capture_output=True,
        text=True,
    )


def _destroy_container(container_name: str):
    subprocess.run(
        shlex.split(f"docker rm -f {container_name}"),
        capture_output=True,
        text=True,
    )


def _reinit_hive_org(hive_url: str, test_config: TestConfig, organisation: str) -> None:
    client = TheHiveApi(
        url=hive_url,
        username=test_config.user,
        password=test_config.password,
        organisation=organisation,
    )

    alerts = client.alert.find()
    cases = client.case.find()

    with ThreadPoolExecutor() as executor:
        executor.map(client.alert.delete, [alert["_id"] for alert in alerts])
        executor.map(client.case.delete, [case["_id"] for case in cases])


def _reinit_hive_admin_org(hive_url: str, test_config: TestConfig) -> None:
    client = TheHiveApi(
        url=hive_url,
        username=test_config.user,
        password=test_config.password,
        organisation=test_config.admin_org,
    )

    users = client.user.find(filters=~Eq("_createdBy", "system@thehive.local"))
    profiles = client.profile.find(filters=~Eq("_createdBy", "system@thehive.local"))
    observable_types = client.observable_type.find(
        filters=~Eq("_createdBy", "system@thehive.local")
    )
    custom_fields = client.custom_field.list()

    with ThreadPoolExecutor() as executor:
        executor.map(client.user.delete, [user["_id"] for user in users])
        executor.map(client.profile.delete, [profile["_id"] for profile in profiles])
        executor.map(
            client.custom_field.delete,
            [custom_field["_id"] for custom_field in custom_fields],
        )
        executor.map(
            client.observable_type.delete,
            [observable_type["_id"] for observable_type in observable_types],
        )


def spawn_hive_container(test_config: TestConfig) -> str:
    if not _is_container_exist(container_name=test_config.container_name):
        _run_container(
            container_name=test_config.container_name,
            container_image=test_config.image_name,
        )
    url = _build_container_url(container_name=test_config.container_name)

    if not _is_container_responsive(container_url=url):
        _destroy_container(container_name=test_config.container_name)
        raise RuntimeError("Unable to startup test container for TheHive")

    return url


def reinit_hive_container(test_config: TestConfig) -> None:
    hive_url = spawn_hive_container(test_config=test_config)
    with ThreadPoolExecutor() as executor:
        for organisation in [
            test_config.main_org,
            test_config.share_org,
        ]:
            executor.submit(_reinit_hive_org, hive_url, test_config, organisation)
        executor.submit(_reinit_hive_admin_org, hive_url, test_config)
