import enum

class Direction(enum.Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Tile(object):
    tiles = {}
    borders = {}

    def __init__(self, tile):
        name, tile = tile.strip("Tile ").split(":\n")
        self.name = name
        tile = [tuple(line) for line in tile.split("\n")]

        self.tiles = []
        for n in range(4):
            rotated = Tile.rotateClockwise(tile, n)
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

    @classmethod
    def rotateClockwise(cls, tile, nr):
        if nr == 0:
            return tile
        elif nr == 1:
            return list(zip(*tile[::-1]))
        else:
            return Tile.rotateClockwise(tile, nr-1)

    def __repr__(self):
        return self.name


with open("example.txt") as file:
    data = file.read()

# Create Tiles
for tile in data.split("\n\n"):
    Tile(tile)

    # print(len(Tile.tiles))

for key, value in Tile.borders.items():
    print(str(key) + ": " + str(value))