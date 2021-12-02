import time

data = [13,16,0,12,15,1]

lastuse = [None] * 30000000

for index, nr in enumerate(data):
    lastuse[nr] = index

newnr = data[-1]

for x in range(6, 30000000):
    lastnr = newnr
    newnr = 0 if lastuse[lastnr] == None else (x-1) - lastuse[lastnr]
    lastuse[lastnr] = x - 1

print("Part 2: " + str(newnr))