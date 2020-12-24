from collections import defaultdict
import timeit

def convertDirToXY(dir):
    nw = dir.count("nw")
    ne = dir.count("ne")
    sw = dir.count("sw")
    se = dir.count("se")
    w = dir.count("w") - nw - sw
    e = dir.count("e") - ne - se
    z = nw - se
    x = e - w - z
    y = ne - sw + z
    return (x, y)

def countNeighbours(x, y):
    return sum([tiles[(x+dX, y+dY)][current] for dX, dY in ((0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1))])

def flip(rounds=1):
    global tiles, current


    for n in range(rounds):
        # for tile in list(tiles):
        #     countNeighbours(*tile)

        for key, value in list(tiles.items()):
            black = value[current]
            black_neighbours = countNeighbours(*key)

            if black and (black_neighbours == 0 or black_neighbours > 2):
                value[not current] = False
            elif not black and black_neighbours == 2:
                value[not current] = True
            else:
                value[not current] = black

        current = not current

def run():
    global current, data, tiles
    with open("input.txt") as file:
        data = [line.strip() for line in file.readlines()]

    current = False
    tiles = defaultdict(lambda: [False, False])

    # Part 1

    for line in data:
        tile = convertDirToXY(line)
        tiles[tile][current] = not tiles[tile][0]

    print("Part 1: " + str(sum(x[0] for x in tiles.values())))

    # Part 2
    for tile in list(tiles):
        countNeighbours(*tile)

    flip(100)
    print("Part 2: " + str(sum(x[current] for x in tiles.values())))

print(timeit.timeit(stmt="run()", setup="from __main__ import run", number=1))