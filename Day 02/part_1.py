import re


test_result = 8


def main(input_file):
    with open(input_file, "r") as f:
        game_lines = f.readlines()

    group_regex = re.compile(r"((\d+) (blue|red|green))")

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    game_ids_sum: int = 0

    for game_id, line in enumerate(game_lines):
        draw_groups = line[(line.find(":") + 2):].split(";")

        game_is_valid = True
    
        for group in draw_groups:
            re_result = re.findall(group_regex, group)
            for draw in re_result:
                if int(draw[1]) > max_cubes[draw[2]]:
                    game_is_valid = False
        
        if game_is_valid:
            game_ids_sum += game_id + 1

    return game_ids_sum

