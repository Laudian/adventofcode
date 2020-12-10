with open("../input.txt") as file:
    data = [int(x) for x in file.readlines()]

data = sorted(data)
data.insert(0, 0)
differences = [0,0,0,1]

for index, value in enumerate(data):
    if index+1 < len(data):
        difference = data[index+1] - value
        differences[difference] += 1
    else:
        pass

print("Part 1: " + str(differences[1] * differences[3]))