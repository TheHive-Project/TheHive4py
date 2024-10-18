#!/usr/bin/env python
import argparse
import subprocess
from typing import Dict


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


def run_build_docs(quiet: bool):
    print("Building thehive4py docs...")
    _run_subprocess(
        command="mkdocs build --clean --strict",
        quiet=quiet,
    )
    print("Successfully built thehive4py docs!")


def run_deploy_docs(quiet: bool):
    print("Deploying thehive4py docs to gh-pages...")
    _run_subprocess(
        command="mike deploy main latest -u -p --allow-empty",
        quiet=quiet,
    )
    print("Successfully deployed thehive4py docs to gh-pages!")


def build_run_options() -> Dict[str, dict]:
    return {
        "build": {"help": "build the package locally", "func": run_build},
        "upload": {"help": "upload the package to pypi", "func": run_upload},
        "build-docs": {"help": "build the docs locally", "func": run_build_docs},
        "deploy-docs": {"help": "deploy the docs to gh-pages", "func": run_deploy_docs},
    }


def parse_arguments(run_options: Dict[str, dict]):
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

    for run_option_name, run_option_attributes in run_options.items():
        parser.add_argument(
            f"--{run_option_name.replace('_', '-')}",
            help=run_option_attributes["help"],
            action="store_true",
        )

    args = parser.parse_args()

    if not any(
        getattr(args, run_option.replace("-", "_")) for run_option in run_options
    ):
        parser.error(f"provide at least one option from: {list(run_options)}")

    return args


def main():
    run_options = build_run_options()
    args = parse_arguments(run_options=run_options)

    quiet = args.quiet

    selected_run_funcs = [
        run_option_attributes["func"]
        for run_option_name, run_option_attributes in run_options.items()
        if getattr(args, run_option_name.replace("-", "_"))
    ]

    for run_func in selected_run_funcs:
        run_func(quiet=quiet)
        print()

    print("Done!")


if __name__ == "__main__":
    main()
