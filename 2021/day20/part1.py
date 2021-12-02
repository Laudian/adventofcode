import math, re

class Tile(object):
    tiles = {}
    borders = {}

    def __init__(self, tile):
        name, tile = tile.strip("Tile ").split(":\n")
        self.name = name
        tile = [tuple(line) for line in tile.split("\n")]

        self.tiles = []
        for n in range(4):
            rotated = tuple(Tile.rotateClockwise(tile, n))
            reverse = tuple(reversed(rotated))
            self.tiles.append(rotated)
            self.tiles.append(reverse)

        self.borders = [tile[0] for tile in self.tiles]
        for border in self.borders:
            if border not in Tile.borders:
                Tile.borders[border] = [self]
            elif self not in Tile.borders[border]:
                Tile.borders[border].append(self)

        Tile.tiles[name] = self
        return

    def __eq__(self, other):
        return self.name == other.name

    def findNeighbours(self):
        neighbours = []
        for border in self.borders[::2]:
            result = Tile.borders[border]
            for tile in result:
                if tile != self:
                    neighbours.append(tile)
        return neighbours

    @classmethod
    def rotateClockwise(cls, tile, nr):
        if nr == 0:
            return tile
        elif nr == 1:
            return list(zip(*tile[::-1]))
        else:
            return list(zip(*Tile.rotateClockwise(tile, nr-1)[::-1]))

    def __repr__(self):
        return self.name


def fillDown(index):
    for n in range(1, size):
        starttile = grid[n-1][index]
        startborder = starttile.actual[-1]
        # Find the other piece with that border
        others = Tile.borders[startborder]
        for tile in others:
            if tile != starttile:
                other: Tile = tile
        # Turn other around so the border we were looking for is on top
        for pattern in other.tiles:
            if pattern[0] == startborder:
                other.actual = pattern
        # Insert tile into grid
        grid[n][index] = other
    return

def fillRight(index):
    for n in range(1, size):
        starttile = grid[index][n-1]
        # We need the border on the right side this time, so we rotate it 3 times and take the upper border
        startborder = Tile.rotateClockwise(starttile.actual, 3)[0]
        # Find the other piece with that border
        others = Tile.borders[startborder]
        for tile in others:
            if tile != starttile:
                other: Tile = tile
        # Turn other around so the border we were looking for is on the left side
        for pattern in other.tiles:
            if pattern[-1] == startborder:
                other.actual = Tile.rotateClockwise(pattern, 1)
        # Insert tile into grid
        grid[index][n] = other
    return



with open("input.txt") as file:
    data = file.read()

# Create Tiles
for tile in data.split("\n\n"):
    Tile(tile)

corners = []

for tile in Tile.tiles.values():
    count = len(tile.findNeighbours())
    if count == 2:
        corners.append(tile)

start = corners[0]

# Turn start so it is the top left corner
# This is the case if neither a pattern nor a 270° rotated pattern have a shared border on top

for pattern in start.tiles:
    if len(Tile.borders[pattern[0]]) == 1 and len(Tile.borders[Tile.rotateClockwise(pattern, 3)[0]]):
        start.actual = pattern
        break

size = int(math.sqrt(len(Tile.tiles)))

grid = [None]*size
for n in range(size):
    grid[n] = [None]*size

# grid[y][x]
grid[0][0] = start

# Fill the Grid with the right tiles
fillDown(0)
for n in range(size):
    fillRight(n)

for x in range(size):
    for y in range(size):
        pattern = grid[y][x].actual
        # Remove upper border
        pattern = pattern[1:]
        # Remove lower border
        pattern = pattern[:-1]
        # Remove left border
        pattern = tuple([line[1:] for line in pattern])
        # Remove right border
        pattern = tuple([line[:-1] for line in pattern])
        grid[y][x] = list(list(line) for line in pattern)

columns = []
for x in range(size):
    columns.append([])
    for y in range(size):
        columns[x] += grid[y][x]

picture = []
for y in range(len(columns[0])):
    picture.append([])
    for x in range(len(columns)):
        picture[y] += columns[x][y]


class Coord2D(tuple):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        return

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coord2D((x, y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Open Monster file
monster_coords = []
with open("monster.txt") as file:
    for index, line in enumerate(file):
        monster_width = len(line)
        monster_height = index+1
        coords = [m.start() for m in re.finditer("#", line)]
        for coord in coords:
            monster_coords.append(Coord2D((coord, index)))


def countMonsters(pattern):
    count = 0
    for x in range(len(pattern[0]) - (monster_width - 1)):
        for y in range(len(pattern) - (monster_height - 1)):
            start = Coord2D((x, y))
            tags = [start + coord for coord in monster_coords]
            monster = True
            for coord in tags:
                if pattern[coord.y][coord.x] != "#":
                    monster = False
                    break
            count += monster
    return count

tagcount = 0
for line in picture:
    for char in line:
        tagcount += char == "#"

for x in range(4):
    rotated = Tile.rotateClockwise(picture, x)
    mirrored = list(reversed(rotated))
    monstercount = countMonsters(rotated)
    monstercount = countMonsters(mirrored
                                 )
print(monstercount)
print(tagcount - monstercount*len(monster_coords))