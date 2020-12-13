with open("../input.txt") as file:
    data = file.readlines()

start = int(data[0])
lines = data[1].split(",")


earliest = None
id = None

for line in lines:
    try:
        line = int(line)
        wait = line - (start % line)
        if not earliest or (wait < earliest):
            earliest = wait
            id = line
    except:
        continue

print("Part 1: " + str(earliest * id))

# Part 2
import math

line_nrs = []
for line in lines:
    try:
        line_nrs.append(int(line))
    except:
        pass

schedule = {}
for nr in line_nrs:
    schedule[nr] = lines.index(str(nr))

kongruenzen = []
for nr in line_nrs:
    kongruenzen.append((nr - schedule[nr]) % nr)

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def chinese(kongruenzen, modulos):
    M = math.prod(modulos)
    m = [int(M/x) for x in modulos]
    e = [gcdExtended(value, m[index])[2]*m[index] for index, value in enumerate(modulos)]
    t = sum([kongruenzen[index]*e[index] for index in range(len(kongruenzen))])
    return t%M

print("Part 2: " + str(chinese(kongruenzen, line_nrs)))