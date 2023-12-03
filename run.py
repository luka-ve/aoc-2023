import os
import importlib
from pathlib import Path
import timeit
from glob import glob
from argparse import ArgumentParser

from colorama import Fore, Back, Style


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "days", nargs="*", type=int, help="Space-separated list of days to run"
    )
    parser.add_argument(
        "-n",
        nargs="?",
        default=1,
        type=int,
        help="Number of repeated runs to average out performance differences between runs",
    )
    parser.add_argument(
        "-f",
        action="store_true",
        help="Forces repeated runs, even for long operations (> 10s)",
    )
    parser.add_argument(
        "-t",
        action="store_true",
        help="Run only on test_input",
    )
    args = parser.parse_args()

    day_folder_pattern = r"Day [0-9][0-9]"
    folders = glob(pathname=day_folder_pattern)
    folders.sort()

    if args.days:
        folders = filter(lambda day: int(day[-2:]) in (args.days), folders)

    for day in folders:
        run_day_folder(day, args.n, args.f, args.t)


def run_day_folder(folder: str, n: int = 1, force: bool = False, test_only: bool = False):
    runtimes = []
    runtimes_info = ""

    for part in (1, 2):
        input_files = []

        if part == 2 and (Path(folder) / "test_input_2.txt").exists():
            input_files.append([Path(folder) / "test_input_2.txt", True])
        else:
            input_files.append([Path(folder) / "test_input.txt", True])

        if not test_only:
            input_files.append([Path(folder) / "input.txt", False])

        # Account for possible differing input between parts
        

        for input_file in input_files:
            is_implemented = True

            for i in range(n):
                start_time = timeit.default_timer()

                part_module = importlib.import_module(f"{folder}.part_{part}")
                try:
                    result = part_module.main(input_file[0].as_posix())

                    runtime = timeit.default_timer() - start_time

                    # Safeguard to not repeat long operations
                    if n > 1 and (runtime < 10 or force):
                        runtimes.append(runtime)
                    else:
                        break
                except NotImplementedError:
                    is_implemented = False
                    continue

            if not is_implemented:
                continue

            if runtimes:
                runtime = sum(runtimes) / len(runtimes)
                runtimes_info = f" on average according to {n} runs. Total runtime: {sum(runtimes):.4f} s"

            print_day_result(
                folder=folder,
                part=part,
                is_test=input_file[1],
                result=result,
                n_runs=n,
                runtime=runtime,
                runtimes=runtimes if runtimes else None,
                module=part_module,
            )


def print_day_result(
    folder=None,
    part=None,
    is_test=None,
    result=None,
    n_runs=None,
    runtime=None,
    runtimes=None,
    module=None,
):
    reset_terminal_colors()

    if is_test:
        test_successful = result == module.test_result

        test_colors = Fore.GREEN if test_successful else Fore.RED
        print("")
        print(
            f"""{test_colors}{test_colors}{folder}.{part} Test {'successful' if test_successful else 'failed'}{Fore.RESET}. Expected -> {module.test_result} : {result} <- Result"""
        )
    else:
        runtimes_info = ""
        if runtimes:
            runtime = sum(runtimes) / len(runtimes)
            runtimes_info = f" {n_runs} runs. Total runtime: {sum(runtimes):.4f} s"

        print(f"{folder}.{part}: Average runtime: {runtime:.4f} s{runtimes_info}")
        print(f"{Fore.BLACK}{Back.WHITE}{result}", end="")

    reset_terminal_colors()
    print("\n", end="")


def reset_terminal_colors():
    print(Style.RESET_ALL, end="")


if __name__ == "__main__":
    main()
