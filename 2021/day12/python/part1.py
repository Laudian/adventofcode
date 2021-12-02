import enum

with open("../input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    # def __init__(self):
    #     self.dir = Direction.EAST

def turn(lr, degree):
    global dir
    turns = degree / 90
    if lr == "L":
        turns *= -1
    dir = Direction((dir.value + turns) % 4)


dir = Direction(Direction.EAST)
dirs = \
    {
        "N" : Direction.NORTH,
        "E" : Direction.EAST,
        "S" : Direction.SOUTH,
        "W" : Direction.WEST

    }
steps = [0, 0, 0, 0]

for line in data:
    letter = line[0]
    number = int(line[1:])
    if letter in "LR":
        turn(letter, number)
    elif letter == "F":
        steps[dir.value] += number
    else:
        steps[dirs[letter].value] += number

print("Part 1: " + str(abs(steps[0]-steps[2]) + abs(steps[1]-steps[3])))