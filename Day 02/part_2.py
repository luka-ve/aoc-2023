import re
import math


test_result = 2286


def main(input_file):
    with open(input_file, "r") as f:
        game_lines = f.readlines()

    group_regex = re.compile(r"((\d+) (blue|red|green))")

    power_sums: int = 0

    for game_id, line in enumerate(game_lines):
        draw_groups = line[(line.find(":") + 2):].split(";")

        mins: dict[str, int] = {
        "red": 0,
        "blue": 0,
        "green": 0
        }
    
        for group in draw_groups:
            re_result = re.findall(group_regex, group)
            for draw in re_result:
                color, value = draw[2], int(draw[1])

                mins[color] = value if mins[color] < value else mins[color]
                
        power_sums += math.prod(mins.values())

    return power_sums

