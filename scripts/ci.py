#!/usr/bin/env python
import argparse
import subprocess
from typing import List


def _run_subprocess(
    command: str,
    init_message: str,
    success_message: str,
    quiet=False,
):
    print(init_message)

    if not quiet:
        stdout = stderr = None
    else:
        stdout = stderr = subprocess.DEVNULL

    import shlex

    try:
        subprocess.run(shlex.split(command), stdout=stdout, stderr=stderr, check=True)
    except subprocess.CalledProcessError as err:
        error_output = (
            f"ERROR: Execution of command '{command}' returned: {err.returncode}\n"
        )
        print(error_output)
        exit(err.returncode)
    else:
        print(success_message, end="\n\n")


def check_all(quiet=False):
    print("Run all checks...")
    check_lint(quiet=quiet)
    check_format(quiet=quiet)
    check_type(quiet=quiet)
    check_cve(quiet=quiet)
    check_security(quiet=quiet)
    print("All checks succeeded!")


def check_lint(quiet=False):
    _run_subprocess(
        command="flake8 thehive4py/ tests/",
        init_message="Run lint checks with flake8...",
        success_message="Lint checks succeeded!",
        quiet=quiet,
    )


def check_format(quiet=False):
    _run_subprocess(
        command="black --check thehive4py/ tests/",
        init_message="Run format checks with black...",
        success_message="Format checks succeeded!",
        quiet=quiet,
    )


def check_type(quiet=False):
    _run_subprocess(
        command="mypy --install-types --non-interactive thehive4py/",
        init_message="Run type checks with mypy...",
        success_message="Type checks succeeded!",
        quiet=quiet,
    )


def check_cve(quiet=False):
    _run_subprocess(
        command="pip-audit .",
        init_message="Run CVE checks with pip-audit...",
        success_message="CVE checks succeeded!",
        quiet=quiet,
    )


def check_security(quiet=False):
    _run_subprocess(
        command="bandit -r thehive4py/",
        init_message="Run security checks with bandit...",
        success_message="Security checks succeeded!",
        quiet=quiet,
    )


def check_test(quiet=False):
    _run_subprocess(
        command="pytest -v --cov",
        init_message="Run integration tests with pytest...",
        success_message="Integration tests succeeded!",
        quiet=quiet,
    )


def build_check_options() -> List[dict]:
    return [
        {"name": "lint", "help": "run lint checks", "check": check_lint},
        {"name": "format", "help": "run format checks", "check": check_format},
        {"name": "type", "help": "run type checks", "check": check_type},
        {"name": "cve", "help": "run cve checks", "check": check_cve},
        {"name": "security", "help": "run security checks", "check": check_security},
        {"name": "test", "help": "run integration tests", "check": check_test},
    ]


def parse_arguments(check_options: List[dict]):
    parser = argparse.ArgumentParser(
        prog="thehive4py-ci",
        description=(
            "run all ci checks except tests by default, "
            "use options to run ci checks selectively"
        ),
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="silence verbose output",
    )
    for check_option in check_options:
        parser.add_argument(
            f"--{check_option['name']}",
            help=check_option["help"],
            action="store_true",
        )

    return parser.parse_args()


def main():
    check_options = build_check_options()
    args = parse_arguments(check_options=check_options)

    quiet = args.quiet

    selective_checks = [
        check_option["check"]
        for check_option in check_options
        if getattr(args, check_option["name"])
    ]

    if selective_checks:
        for check in selective_checks:
            check(quiet=quiet)
    else:
        check_all(quiet=quiet)
    print()


if __name__ == "__main__":
    main()
