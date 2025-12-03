input = open("2015/day1/input.txt", encoding="utf-8").read().strip()

floor = 0

for index, char in enumerate(input):
    if char == ")":
        floor = floor - 1
    elif char == "(":
        floor = floor + 1

    if floor < 0:
        print(f"Santa enters the basemnt at: {index + 1}")
        break
