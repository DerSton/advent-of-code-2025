input = open("day2/input.txt", "r", encoding="utf-8").read().split(",")

result = []

for line in input:
    start, end = line.split("-")[0], line.split("-")[1]
    
    print(f"Processing range: {start} to {end}")
    
    for i in range(int(start), int(end) + 1):
        # find if number pattern repeats at least once
        #Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
        number = str(i)
        length = len(number)
        is_invalid = False
        for size in range(1, length // 2 + 1):
            if length % size == 0:
                pattern = number[:size]
                if pattern * (length // size) == number:
                    is_invalid = True
                    break
        if is_invalid:
            result.append(number)
            print(f"Found invalid ID: {number}")

print(f"Total invalid IDs found: {len(result)} sum to {sum(int(x) for x in result)}")
