with open("../input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def __repr__(self):
        return "({x}|{y})".format(x=self.x, y=self.y)

    def rotateRight(self):
        global position
        newX = self.y
        self.y = self.x * -1
        self.x = newX
        return

    def rotate(self, lr, degree):
        rotations = (degree / 90) % 4
        if lr == "L":
            rotations = 4-rotations
        for i in range(int(rotations)):
            self.rotateRight()
        return



dirs = \
    {
        "N" : Coordinate(0, 1),
        "E" : Coordinate(1, 0),
        "S" : Coordinate(0, -1),
        "W" : Coordinate(-1, 0)
    }


waypoint = Coordinate(10, 1)
position = Coordinate(0, 0)

for line in data:
    letter = line[0]
    number = int(line[1:])
    if letter in "LR":
        waypoint.rotate(letter, number)
    elif letter == "F":
        position = position + waypoint * number
    else:
        waypoint = waypoint + dirs[letter] * number

print(position)
print("Part 2: " + str(abs(position.x) + abs(position.y)))