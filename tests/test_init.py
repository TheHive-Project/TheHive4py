import sys

import pytest

from thehive4py import _warn_old_py_version


def test_warn_old_py_version():
    actual_py_version = sys.version_info
    dummy_min_py_version = (actual_py_version[0], actual_py_version[1] + 1)
    with pytest.deprecated_call():
        _warn_old_py_version(min_py_version=dummy_min_py_version)
