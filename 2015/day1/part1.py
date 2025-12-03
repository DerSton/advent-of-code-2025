input = open("2015/day1/input.txt", encoding="utf-8").read().strip()

floor = 0

for char in input:
    if char == ")":
        floor = floor - 1
    elif char == "(":
        floor = floor + 1

    print(f"Current floor: {floor}")

print(f"Final floor: {floor}")
