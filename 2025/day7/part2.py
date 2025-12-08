import sys
sys.setrecursionlimit(2000000000)

input = open("2025/day7/input.txt", "r", encoding="utf-8").read().splitlines()

timelines = 0

def spawn_timeline(row: int, col: int, input, timelines):
    timelines = timelines + 1
    while row < len(input) and not input[row][col] == "^":
        row = row + 1
    if row == len(input) - 1:
        return 
    spawn_timeline(row, col-1, input, timelines)
    spawn_timeline(row, col+1, input, timelines)

spawn_timeline(1, 70, input, timelines)

print(timelines)
