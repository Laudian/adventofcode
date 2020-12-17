import itertools

class Coord3D(tuple):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        return

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Coord3D((x, y, z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def getNeighbours(self):
        directions = [Coord3D(x) for x in itertools.product([-1, 0, 1], repeat=3)]
        directions.remove(Coord3D((0,0,0)))
        neighbours = [direction + self for direction in directions]
        return neighbours


board = {}

with open("input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

for lineindex, line in enumerate(data):
    for charindex, char in enumerate(line):
        coords = Coord3D((charindex, lineindex, 0))
        board[coords] = True if char == "#" else False

#
copy = list(board)
for field in copy:
    for neighbour in field.getNeighbours():
        if neighbour not in board:
            board[neighbour] = False

def iterate(iterations):
    global board

    for x in range(iterations):
        copy = dict(board)
        for field in copy:
            activecount = 0
            neighbours = field.getNeighbours()
            for neighbour in neighbours:
                if neighbour in copy:
                    activecount += copy[neighbour]
                else:
                    board[neighbour] = False
            board[field] = True if activecount == 3 or (activecount == 2 and copy[field]) else False

iterate(6)
print(list(board.values()).count(True))