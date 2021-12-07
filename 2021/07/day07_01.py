import math

with open("input.txt") as file:
    puzzle = sorted([int(x) for x in file.read().split(",")])


cost_1 = lambda distance: distance
cost_2 = lambda distance: int(0.5 * distance * (distance + 1))


def fuel_consumption(target_pos, puzzle, cost):
    fuel = 0
    for pos in puzzle:
        distance = abs(pos - target_pos)
        fuel += cost(distance)

    return fuel

median = puzzle[len(puzzle) // 2]
print("Part 1: " + str(fuel_consumption(median, puzzle, cost_1)))

mean = sum(puzzle)/len(puzzle)
fuel_2 = min(fuel_consumption(math.floor(mean), puzzle, cost_2), fuel_consumption(math.ceil(mean), puzzle, cost_2))
print("Part 2: " + str(fuel_2))
