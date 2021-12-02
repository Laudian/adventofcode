import itertools

with open("../input.txt") as file:
    data = [int(x) for x in file.readlines()]

data = sorted(data)
data.insert(0, 0)
data.append(data[-1]+3)
differences = [0,0,0,0]
unskippable = [0]

for index, value in enumerate(data):
    if index+1 < len(data):
        difference = data[index+1] - value
        differences[difference] += 1
        if difference == 3:
            if value not in unskippable:
                unskippable.append(value)
            unskippable.append(data[index+1])
    else:
        pass

print("Part 1: " + str(differences[1] * differences[3]))

# Part 2

def possiblePath(start, end, path):
    if not path: return end - start <= 3
    if not path[0] - start <= 3: return False
    for index, value in enumerate(path):
        if index+1 < len(path):
            if not path[index+1]-value <= 3: return False
    if not end - path[-1] <= 3: return False
    return True


def paths(start, end):
    result = 0
    start_index = data.index(start)
    end_index = data.index(end)
    between = data[start_index+1:end_index]
    for x in range(0, len(between)+1):
        for combination in itertools.combinations(between, x):
            if possiblePath(start, end, combination):
                result += 1
    return result


result=1

for x in range(0, len(unskippable)-2):
    start = unskippable[x]
    end = unskippable[x+1]
    result *= paths(start, end)
print("Part 2: " +  str(result))
