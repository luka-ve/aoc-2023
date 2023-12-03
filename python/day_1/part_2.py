import re

with open("python/day_1/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


# Lookahead assertion
regex_pattern = re.compile("(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

mapping_table = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

keys = list(mapping_table.keys())

result = 0
for line in inp:
    first_match = ""
    for i, matches in enumerate(re.finditer(regex_pattern, line)):
        if i == 0:
            match0 = matches.group(1) if matches.group(1) not in keys else mapping_table[matches.group(1)]
    
    match1 = matches.group(1) if matches.group(1) not in keys else mapping_table[matches.group(1)]
    newval = int(f"{match0}{match1}")
    result += newval

print(result)
