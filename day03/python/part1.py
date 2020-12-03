with open("../input03.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

class Map(object):
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def at(self, x, y):
        if y >= self.height:
            return "end"
        return self.data[y][x % self.width]

    def path(self, paramX, paramY):
        x , y, counter = 0, 0, 0

        while True:
            result = self.at(x, y)
            if result == "end":
                return counter
            elif result == "#":
                counter += 1
            x += paramX
            y += paramY

map = Map(data)
print("Part 1: " + str(map.path(3, 1)))

part2 = map.path(1,1)*map.path(3,1)*map.path(5,1)*map.path(7,1)*map.path(1,2)
print("Part 2: " + str(part2))