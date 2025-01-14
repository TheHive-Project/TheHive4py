from thehive4py.client import TheHiveApi


def _warn_old_py_version(min_py_version=(3, 9)):
    import sys
    import warnings

    if sys.version_info < min_py_version:
        warnings.warn(
            message=(
                "thehive4py will drop support for Python versions below "
                f"{min_py_version[0]}.{min_py_version[1]}, as they have reached their "
                "end of life. Please upgrade to a newer version as soon as possible."
            ),
            category=DeprecationWarning,
            stacklevel=3,
        )


_warn_old_py_version()
