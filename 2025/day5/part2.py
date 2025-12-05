input = open("2025/day5/input.txt", "r", encoding="utf-8").read().splitlines()

fresh = input[:186]

for index, entry in enumerate(fresh):
    new_range = (int(entry.split("-")[0]), int(entry.split("-")[1]))
    new_range = tuple(sorted(new_range))
    fresh[index] = new_range

fresh.sort()

current_start, current_end = fresh[0]
merged_ranges = []

for start, end in fresh[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end

merged_ranges.append((current_start, current_end))
total_count = sum(end - start + 1 for start, end in merged_ranges)

print(total_count)
