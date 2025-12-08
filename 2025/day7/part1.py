input = open("2025/day7/input.txt", "r", encoding="utf-8").read().splitlines()

beams = [True if col == "S" else False for col in input[0]]
split_times = 0

for row in input[0:]:
    print("".join(["|" if beam else "." for beam in beams]))
    for index, col in enumerate(row):
        if col == "^":
            if not beams[index]:
                continue
            beams[index] = False
            beams[index-1] = True
            beams[index+1] = True
            split_times = split_times + 1

print(split_times)
