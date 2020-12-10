with open("../input07.txt") as file:
    data = [line.strip(".\n").replace("bags", "bag") for line in file.readlines()]

mydict = {}

for index, line in enumerate(data):
    parent, children = line.split(" contain")
    children = children.strip(" ").split(", ")
    for index2, child in enumerate(children):
        amount, color = child.split(" ", 1)
        children[index2] = (amount, color)
    mydict[parent] = children

def content(color):
    result = 1
    bags = mydict[color]
    for bag in bags:
        if bag[0] == "no":
            pass
        else:
            result += int(bag[0]) * content(bag[1])
    return result

def parents(colorp):
    for color in mydict:
        colors = [color2 for amount, color2 in mydict[color]]
        if colorp in colors and color not in bags:
            to_process.append(color)
            bags.append(color)

bags = []
to_process = []


parents("shiny gold bag")
while len(to_process) > 0:
    parents(to_process.pop())


print("Part 1: " + str(len(bags)))
print("Part 2: " + str(content("shiny gold bag")-1))