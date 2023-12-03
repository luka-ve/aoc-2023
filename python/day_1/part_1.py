import re

with open("python/day_1/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


regex_pattern = "\d"
result = 0
for line in inp:
    matches: list[str] = re.findall("\d", line)
    result += int(f"{matches[0]}{matches[-1]}")

print(result)
