import re


test_result = 142


def main(input_file):
    with open(input_file) as f:
        inp = [line.strip() for line in f.readlines()]


    regex_pattern = "\d"
    result = 0
    for line in inp:
        matches: list[str] = re.findall("\d", line)
        result += int(f"{matches[0]}{matches[-1]}")

    return result
