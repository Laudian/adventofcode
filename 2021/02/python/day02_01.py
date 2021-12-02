from collections import defaultdict

with open("../input.txt") as file:
    puzzle = [(command, int(value)) for command, value in [line.split() for line in file.readlines()]]

result = defaultdict(lambda: 0)
for command, value in puzzle:
    result[command] += value

print("Part 1: " + str((result["down"]-result["up"]) * result["forward"]))


def process(command, value, result):
    if command == "forward":
        result["pos"] += value
        result["depth"] += value * result["aim"]
    else:
        result["aim"] += value if command == "down" else value*-1

result = defaultdict(lambda: 0)

for command, value in puzzle:
    process(command, value, result)

print("part 2: " + str(result["pos"] * result["depth"]))
