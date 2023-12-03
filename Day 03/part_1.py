import re


test_result = 4361


def main(input_file):
    with open(input_file, "r") as f:
        symbols = [line.strip().replace(".", " ") for line in f.readlines()]


    line_length = len(symbols[0])
    
    parts_sum = 0

    for line_i, line in enumerate(symbols):
        for match in re.finditer(r"\d+", line):
            match: re.Match
            

            h_from = max(match.start() - 1, 0)
            h_to = min(match.end() + 1, line_length)

            line_before = symbols[max(line_i - 1, 0)][h_from:h_to] if line_i > 0 else ""
            same_line = symbols[line_i][h_from:h_to]
            line_after = symbols[max(line_i + 1, 0)][h_from:h_to] if line_i < (len(symbols) - 1) else ""

            has_symbol = re.match(r".*\D.*",
                    (line_before + same_line + line_after).replace(" ", "")
                    )
            if has_symbol:
                parts_sum += int(match.group())
    
    return parts_sum

            