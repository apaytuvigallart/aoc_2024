import os
import re


def mul(first: int, second: int) -> int:
    multiplication = first * second
    return multiplication


abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)

with open(f"{dir_path}/input.txt") as f:
    lines = f.readlines()

list_of_matches = []
result = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

for line in lines:
    matches = re.finditer(pattern, str(line))  # find all matches
    list_of_matches.extend(
        match.group(0) for match in matches
    )  # for each match, extend the list

# get the first and second number of each match and multiply it. Then, sum the output to result
for match in list_of_matches:
    first = int(match[4 : match.index(",")])
    second = int(match[match.index(",") + 1 : -1])
    result += mul(first, second)

print(result)
