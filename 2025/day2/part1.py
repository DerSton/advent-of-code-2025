input = open("day2/input.txt", "r", encoding="utf-8").read().split(",")

result = []

for line in input:
    start, end = line.split("-")[0], line.split("-")[1]
    
    print(f"Processing range: {start} to {end}")
    
    for i in range(int(start), int(end) + 1):
        number = str(i)
        if len(number) % 2 != 0:
            continue
        
        if number[:len(number)//2] == number[len(number)//2:]:
            result.append(number)
            print(f"Found invalid ID: {number}")

print(f"Total invalid IDs found: {len(result)} sum to {sum(int(x) for x in result)}")
