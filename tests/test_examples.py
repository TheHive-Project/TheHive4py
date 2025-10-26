import importlib
import runpy
from pathlib import Path

import pytest

from thehive4py import TheHiveApi

_examples_dir = Path(__file__).parent.parent / "examples"
_excluded_example_paths = []
_example_paths = sorted(
    [
        example_path
        for example_path in _examples_dir.rglob("*.py")
        if example_path not in _excluded_example_paths
    ]
)


def _patch_thehiveapi_symbol(monkeypatch: pytest.MonkeyPatch, thehive: TheHiveApi):
    """Patch TheHiveApi symbol in thehive4py modules to return the test client."""

    # Patch the package-level symbol so "from thehive4py import TheHiveApi" yields our test client
    thehive4py_lib = importlib.import_module("thehive4py")
    monkeypatch.setattr(
        thehive4py_lib, "TheHiveApi", lambda *a, **k: thehive, raising=False
    )

    # Also patch the client module symbol in case examples import from thehive4py.client
    try:
        thehive4py_client_mod = importlib.import_module("thehive4py.client")
        monkeypatch.setattr(
            thehive4py_client_mod,
            "TheHiveApi",
            lambda: thehive,
            raising=False,
        )
    except ModuleNotFoundError:
        # ignore if client module isn't present in this environment
        pass


@pytest.mark.parametrize(
    "example_path",
    _example_paths,
    ids=[
        str(example_path.relative_to(_examples_dir)) for example_path in _example_paths
    ],
)
def test_examples(
    example_path: Path, thehive: TheHiveApi, monkeypatch: pytest.MonkeyPatch
):
    """Execute each example file and consider it correct if exits without error.

    The global TheHiveApi symbol is patched so examples that do:
        from thehive4py import TheHiveApi
    or
        from thehive4py.client import TheHiveApi
    will receive the test client (thehive fixture) instead of creating a real client.
    """

    _patch_thehiveapi_symbol(monkeypatch, thehive)

    # Run the example as a script; use __main__ so top-level guards run as expected
    try:
        runpy.run_path(str(example_path), run_name="__main__")
    except Exception as exc:
        pytest.fail(f"Example {example_path} raised an exception: {exc}")
