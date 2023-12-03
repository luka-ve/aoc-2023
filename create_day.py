import os
from shutil import copyfile
from glob import glob
from argparse import ArgumentParser
from datetime import date
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument("day", nargs="?", type=int)
    args = parser.parse_args()
    day = args.day

    if not args.day:
        day = date.today().day

    # Create folder and files
    day_path = Path(__file__).parent / f"Day {day:02}"

    day_path.mkdir(exist_ok=True)
    templates_folder = Path(__file__).parent / "Day_Template"
    for f in os.listdir(
        templates_folder.as_posix(),
    ):
        copyfile(templates_folder / f, day_path / f)


if __name__ == "__main__":
    main()
