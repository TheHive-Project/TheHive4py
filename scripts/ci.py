#!/usr/bin/env python
import argparse
import subprocess


def _run_subprocess(
    args: str,
    init_message: str,
    success_message: str,
    error_message: str,
    verbose=False,
):
    print(init_message)
    proc = subprocess.run(args, shell=True, capture_output=True)

    process_output = proc.stdout.decode() or proc.stderr.decode()
    indented_process_output = "\n".join(
        [f"\t{output_line}" for output_line in process_output.splitlines()]
    )

    if proc.returncode != 0:
        exit_message = "\n".join([error_message, indented_process_output])
        exit(exit_message)

    if verbose:
        print(indented_process_output)

    print(success_message)


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
        args="flake8 thehive4py/ tests/",
        init_message="Run lint checks with flake8...",
        success_message="Lint checks succeeded!",
        error_message="Lint checks failed due to:",
        verbose=verbose,
    )


def check_format(verbose=False):
    _run_subprocess(
        args="black --diff thehive4py/ tests/",
        init_message="Run format checks with black...",
        success_message="Format checks succeeded!",
        error_message="Lint checks failed due to:",
        verbose=verbose,
    )


def check_type(verbose=False):
    _run_subprocess(
        args="mypy --install-types --non-interactive thehive4py/",
        init_message="Run type checks with mypy...",
        success_message="Type checks succeeded!",
        error_message="Type checks failed due to:",
        verbose=verbose,
    )


def check_cve(verbose=False):
    _run_subprocess(
        args="pip-audit .",
        init_message="Run CVE checks with pip-audit...",
        success_message="CVE checks succeeded!",
        error_message="CVE checks failed due to:",
        verbose=verbose,
    )


def check_security(verbose=False):
    _run_subprocess(
        args="bandit -r thehive4py/",
        init_message="Run security checks with bandit...",
        success_message="Security checks succeeded!",
        error_message="Security checks failed due to:",
        verbose=verbose,
    )


def parse_arguments():
    main_parser = argparse.ArgumentParser(
        prog="thehive4py-ci",
        description=(
            "run all ci checks or use sub commands to run ci checks individually"
        ),
    )
    main_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="generate verbose output",
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
    args.func(verbose=args.verbose)


if __name__ == "__main__":
    main()
