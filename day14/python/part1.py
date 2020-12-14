with open("../input.txt") as file:
    ops = file.readlines()

memory = {}

def intTo36Bit(nr):
    return format(int(nr), "b").rjust(36, "0")

def applyMask(mask, value):
    result = [x if (mask[index] == "X") else mask[index] for index, x in enumerate(value)]
    return int("".join(result), 2)

for op in ops:
    name, value = op.split(" = ")
    if name == "mask":
        mask = value
    else:
        masked_value = applyMask(mask, intTo36Bit(value))
        memory[name[4:-1]] = masked_value

print("Part 1: " + str(sum(memory.values())))

# Part 2
import itertools

def applyMask(mask, value):
    result = [x if (mask[index] == "0") else mask[index] for index, x in enumerate(value)]
    xcount = result.count("X")
    for bits in itertools.product(("0", "1"), repeat=xcount):
        bits = list(bits)
        copy = list(result)
        for index, element in enumerate(copy):
            if element == "X":
                copy[index] = bits.pop()
        yield int("".join(copy), 2)

memory = {}

for op in ops:
    name, value = op.split(" = ")
    if name == "mask":
        mask = value
    else:
        addresses = applyMask(mask, intTo36Bit(name[4:-1]))
        for address in addresses:
            memory[address] = int(value)

print("Part 2: " + str(sum(memory.values())))