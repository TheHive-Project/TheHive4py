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


def run_all(verbose=False):
    print("Run all deployment tasks...")
    run_build(verbose=verbose)
    run_publish(verbose=verbose)
    print("All tasks succeeded!")


def run_build(verbose: bool):
    _run_subprocess(
        args=("rm -rf build/ dist/ && python -m build --sdist --wheel"),
        init_message="Building the package with the build module...",
        success_message="Package build succeeded!",
        error_message="Package build failed due to:",
        verbose=verbose,
    )


def run_publish(verbose: bool):
    _run_subprocess(
        args=("echo 'Publish command is not implemented yet...' && exit 1 "),
        init_message="Publishing the package with twine...",
        success_message="Publish succeeded!",
        error_message="Publish failed due to:",
        verbose=verbose,
    )


def parse_arguments():
    main_parser = argparse.ArgumentParser(
        prog="thehive4py-cd",
        description="run all cd tasks or use sub commands to run cd tasks individually",
    )
    main_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="generate verbose output",
    )
    main_parser.set_defaults(func=run_all)

    subparsers = main_parser.add_subparsers(help="commands")
    subparser_options = [
        {
            "name": "build",
            "help": "task to build the package",
            "default_func": run_build,
        },
        {
            "name": "publish",
            "help": "task to publish the package",
            "default_func": run_publish,
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
