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
