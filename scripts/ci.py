#!/usr/bin/env python
import argparse
import subprocess
from typing import List


def _run_subprocess(
    command: str,
    quiet=False,
):
    if not quiet:
        stdout = stderr = None
    else:
        stdout = stderr = subprocess.DEVNULL

    try:
        subprocess.run(str.split(command), stdout=stdout, stderr=stderr, check=True)
    except subprocess.CalledProcessError as err:
        error_output = (
            f"ERROR: Execution of command '{command}' returned: {err.returncode}\n"
        )
        print(error_output)
        exit(err.returncode)


def check_all(quiet=False):
    print("Run all checks...")
    check_lint(quiet=quiet)
    check_format(quiet=quiet)
    check_type(quiet=quiet)
    check_cve(quiet=quiet)
    check_security(quiet=quiet)
    print("All checks succeeded!")


def check_lint(quiet=False):
    print("Run lint checks with flake8...")
    _run_subprocess(
        command="flake8 thehive4py/ tests/",
        quiet=quiet,
    )
    print("Lint checks succeeded!")


def check_format(quiet=False):
    print("Run format checks with black...")
    _run_subprocess(
        command="black --check thehive4py/ tests/",
        quiet=quiet,
    )
    print("Format checks succeeded!")


def check_type(quiet=False):
    print("Run type checks with mypy...")
    _run_subprocess(
        command="mypy --install-types --non-interactive thehive4py/",
        quiet=quiet,
    )
    print("Type checks succeeded!")


def check_cve(quiet=False):
    print("Run CVE checks with pip-audit...")
    _run_subprocess(
        command="pip-audit .",
        quiet=quiet,
    )
    print("CVE checks succeeded!")


def check_security(quiet=False):
    print("Run security checks with bandit...")
    _run_subprocess(
        command="bandit -r thehive4py/",
        quiet=quiet,
    )
    print("Security checks succeeded!")


def check_test(quiet=False):
    print("Run integration tests with pytest...")
    _run_subprocess(
        command="pytest -v --cov",
        quiet=quiet,
    )
    print("Integration tests succeeded!")


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


if __name__ == "__main__":
    main()
