with open("../input01.txt") as file:
    data = [int(x) for x in file.readlines()]

def findTwo(target, data):
    for value in data:
        difference = target - value
        if difference in data:
            return(difference * value);
    return False

def findThree(target, data):
    for index, value in enumerate(data):
        difference = target - value
        result = findTwo(difference, data[index:])
        if result:
            return value * result

print("Part 1: " + str(findTwo(2020, data)))
print("Part 2: " + str(findThree(2020, data)))