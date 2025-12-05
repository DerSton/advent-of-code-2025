input = open("2025/day5/input.txt", "r", encoding="utf-8").read().splitlines()

fresh = input[:186]
availables = input[187:]

for index, entry in enumerate(fresh):
    fresh[index] = [int(entry.split("-")[0]), int(entry.split("-")[1])]
    
for index, available in enumerate(availables):
    availables[index] = int(available)


fresh_sum = 0

for available in availables:
    for fresh_range in fresh:
        n_range = fresh_range
        n_range.sort
        if fresh_range[0] <= available <= fresh_range[1]:
            fresh_sum = fresh_sum + 1
            break

print(fresh_sum)
