with open("../input.txt") as file:
    puzzle = [int(line) for line in file.readlines()]

counter = 0
for index in range(1, len(puzzle)):
    counter += puzzle[index] > puzzle[index-1]

print("Part 1: " + str(counter))

counter = 0
for index in range(3, len(puzzle)):
    counter += puzzle[index] > puzzle[index-3]

print("Part 2: " + str(counter))