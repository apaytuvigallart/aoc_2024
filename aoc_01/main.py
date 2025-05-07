import os

abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)

with open(f"{dir_path}/input.txt") as f:
    lines = f.readlines()
    left_list, right_list = zip(*(map(int, line.split()) for line in lines))

ordered_left = sorted(left_list)
ordered_right = sorted(right_list)
difference = 0

for left, right in zip(ordered_left, ordered_right):
    difference += abs(left - right)

print(f"Difference: {difference}")
