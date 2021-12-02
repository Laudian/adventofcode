with open("../input.txt") as file:
    data = [list(line.strip("\n")) for line in file.readlines()]

sizeX = len(data[0])
sizeY = len(data)

def occupiedNeighbours(paramX, paramY):
    counter = 0
    for x in range(paramX - 1, paramX + 2):
        for y in range(paramY - 1, paramY + 2):
            if (not ((x == paramX) and (y == paramY))) and (((x>=0) and (y>=0))):
                try:
                    counter += (data[y][x] == "#")
                except:
                    pass
    return counter

while True:
    new_data = [list(line) for line in data]
    for x in range(sizeX):
        for y in range(sizeY):
            status = data[y][x]
            count = occupiedNeighbours(x, y)
            if status == "L" and count == 0:
                new_data[y][x] = "#"
            elif status == "#" and count >= 4:
                new_data[y][x] = "L"
    if data == new_data:
        break
    else:
        data = new_data

count = 0
for line in data:
    count += line.count("#")
print("Part 1: " + str(count))

# Part 2

with open("../input.txt") as file:
    data = [list(line.strip("\n")) for line in file.readlines()]

sizeX = len(data[0])
sizeY = len(data)

def occupiedInLOS(paramX, paramY):
    counter = 0
    dirs = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
    for dir in dirs:
        x = paramX + dir[0]
        y = paramY + dir[1]
        while (0 <= x < sizeX) and (0 <= y < sizeY):
            if data[y][x] != ".":
                counter += data[y][x] == "#"
                break
            x += dir[0]
            y += dir[1]
    return counter


counter = 0
while True:
    new_data = [list(line) for line in data]
    for x in range(sizeX):
        for y in range(sizeY):
            status = data[y][x]
            count = occupiedInLOS(x, y)
            if status == "L" and count == 0:
                new_data[y][x] = "#"
            elif status == "#" and count >= 5:
                new_data[y][x] = "L"
    if data == new_data:
        break
    else:
        data = new_data

count = 0
for line in data:
    count += line.count("#")
print("Part 2: " + str(count))