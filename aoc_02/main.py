import os


def review_report(line: list) -> str:
    if all(a < b and b - a <= 3 for a, b in zip(line, line[1:])):
        return True

    if all(a > b and a - b <= 3 for a, b in zip(line, line[1:])):
        return True

    return False


safe_reports = 0
abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)

with open(f"{dir_path}/input.txt") as f:
    lines = f.readlines()

for line in lines:
    line_list = list(map(int, line.split()))

    if review_report(line=line_list) is True:
        safe_reports += 1

print(safe_reports)
