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


def run_all(quiet=False):
    print("Run all deployment tasks...")
    run_build(quiet=quiet)
    run_upload(quiet=quiet)
    print("All tasks succeeded!")


def run_build(quiet: bool):
    print("Building thehive4py with the build module...")
    _run_subprocess(
        command="rm -rf build/ dist/",
        quiet=quiet,
    )
    _run_subprocess(
        command="python -m build --sdist --wheel",
        quiet=quiet,
    )
    print("Successfully built thehive4py!")


def run_upload(quiet: bool):
    print("Publishing thehive4py with twine...")
    _run_subprocess(
        command="twine upload dist/*",
        quiet=quiet,
    )
    print("Successfully published thehive4py!")


def build_run_options() -> List[dict]:
    return [
        {"name": "build", "help": "run build step", "func": run_build},
        {"name": "upload", "help": "run upload step", "func": run_upload},
    ]


def parse_arguments(run_options: List[dict]):
    parser = argparse.ArgumentParser(
        prog="thehive4py-cd",
        description="run all cd steps or use options to run cd steps selectively",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="silence verbose output",
    )

    for run_option in run_options:
        parser.add_argument(
            f"--{run_option['name']}",
            help=run_option["help"],
            action="store_true",
        )

    return parser.parse_args()


def main():
    run_options = build_run_options()
    args = parse_arguments(run_options=run_options)

    quiet = args.quiet

    selective_runs = [
        run_option["func"]
        for run_option in run_options
        if getattr(args, run_option["name"])
    ]

    if selective_runs:
        for run in selective_runs:
            run(quiet=quiet)
    else:
        run_all(quiet=quiet)


if __name__ == "__main__":
    main()
