from collections import defaultdict
from itertools import chain
from functools import reduce


with open("input.txt") as file:
    puzzle = [line.strip() for line in file]


def process(line, board1, board2):
    # Very ugly nested list comprehension to split input and convert to int
    x1, y1, x2, y2 = [int(nr) for nr in line.replace(" -> ", ",").split(",")]

    # Horizontal
    if x1 == x2:
        start, stop = sorted((y1, y2))
        for y in range(start, stop+1):
            board1[(x1, y)] += 1
            board2[(x1, y)] += 1

    # Vertical
    elif y1 == y2:
        start, stop = sorted((x1, x2))
        for x in range(start, stop+1):
            board1[(x, y1)] += 1
            board2[(x, y1)] += 1

    # Diagonal
    else:
        start_x, stop_x = (x1, x2) if (flag := x2 > x1) else (x2, x1)
        start_y, stop_y = (y1, y2) if flag else (y2, y1)
        increment_y = 1 if stop_y > start_y else -1
        for n in range(stop_x-start_x+1):
            board2[(start_x+n, start_y+n*increment_y)] += 1


board1 = defaultdict(lambda: 0)
board2 = defaultdict(lambda: 0)

for line in puzzle:
    process(line, board1, board2)

value1 = reduce(lambda a, b: a + (b >= 2), board1.values(), 0)
value2 = reduce(lambda a, b: a + (b >= 2), board2.values(), 0)

print("Part 1: " + str(value1))
print("Part 2: " + str(value2))
