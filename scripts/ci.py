#!/usr/bin/env python
import argparse
import subprocess


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


def check_all(verbose=False):
    print("Run all checks...")
    check_lint(verbose=verbose)
    check_format(verbose=verbose)
    check_type(verbose=verbose)
    check_cve(verbose=verbose)
    check_security(verbose=verbose)
    print("All checks succeeded!")


def check_lint(verbose=False):
    _run_subprocess(
        command="flake8 thehive4py/ tests/",
        init_message="Run lint checks with flake8...",
        success_message="Lint checks succeeded!",
        quiet=verbose,
    )


def check_format(verbose=False):
    _run_subprocess(
        command="black --check thehive4py/ tests/",
        init_message="Run format checks with black...",
        success_message="Format checks succeeded!",
        quiet=verbose,
    )


def check_type(verbose=False):
    _run_subprocess(
        command="mypy --install-types --non-interactive thehive4py/",
        init_message="Run type checks with mypy...",
        success_message="Type checks succeeded!",
        quiet=verbose,
    )


def check_cve(verbose=False):
    _run_subprocess(
        command="pip-audit .",
        init_message="Run CVE checks with pip-audit...",
        success_message="CVE checks succeeded!",
        quiet=verbose,
    )


def check_security(verbose=False):
    _run_subprocess(
        command="bandit -r thehive4py/",
        init_message="Run security checks with bandit...",
        success_message="Security checks succeeded!",
        quiet=verbose,
    )


def run_test(verbose=False):
    _run_subprocess(
        command="pytest -v --cov",
        init_message="Run integration tests with pytest...",
        success_message="Integration tests succeeded!",
        quiet=verbose,
    )


def parse_arguments():
    main_parser = argparse.ArgumentParser(
        prog="thehive4py-ci",
        description=(
            "run all ci checks or use sub commands to run ci checks individually"
        ),
    )
    main_parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="silence verbose output",
    )
    main_parser.set_defaults(func=check_all)

    subparsers = main_parser.add_subparsers(help="commands")
    subparser_options = [
        {"name": "lint", "help": "run lint checks only", "default_func": check_lint},
        {
            "name": "format",
            "help": "run format checks only",
            "default_func": check_format,
        },
        {"name": "type", "help": "run type checks only", "default_func": check_type},
        {"name": "cve", "help": "run cve checks only", "default_func": check_cve},
        {
            "name": "security",
            "help": "run security checks",
            "default_func": check_security,
        },
        {
            "name": "test",
            "help": "run integration tests",
            "default_func": run_test,
        },
    ]

    for subparser_option in subparser_options:
        _subparser = subparsers.add_parser(
            name=subparser_option["name"],
            help=subparser_option["help"],
            parents=[main_parser],
            add_help=False,
        )
        _subparser.set_defaults(func=subparser_option["default_func"])

    return main_parser.parse_args()


def main():
    args = parse_arguments()
    args.func(verbose=args.quiet)


if __name__ == "__main__":
    main()
