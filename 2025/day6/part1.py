import math

input = open("2025/day6/input.txt", "r", encoding="utf-8").read().splitlines()

def parse_row(row: str, is_number: bool = False):
    split = row.split(" ")
    split = [int(split.strip()) if is_number else split.strip() for split in split if split != ""]
    return split

numbers1 = parse_row(input[0], True)
numbers2 = parse_row(input[1], True)
numbers3 = parse_row(input[2], True)
numbers4 = parse_row(input[3], True)
operations = parse_row(input[4])

summe = 0

for index, operation in enumerate(operations):
    numbers = numbers1[index], numbers2[index], numbers3[index], numbers4[index]
    match operation:
        case "+":
            summe = summe + sum(numbers)
            continue
        case "*":
            summe = summe + math.prod(numbers)
            continue

print(summe)
