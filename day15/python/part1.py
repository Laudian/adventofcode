import time

data = [13,16,0,12,15,1]

lastuse = [0] * 30000000
usecount = [0] * 30000000

for index, nr in enumerate(data):
    lastuse[nr] = index
    usecount[nr] += 1
    newnr = nr

for x in range(len(data), 2020):
    lastnr = newnr
    newnr = 0 if usecount[lastnr] == 0 else (x-1) - lastuse[lastnr]
    lastuse[lastnr] = x - 1
    usecount[lastnr] += 1

print("Part 1: " + str(newnr))

start = time.time()

lastuse = [0] * 30000000
usecount = [0] * 30000000

for index, nr in enumerate(data):
    lastuse[nr] = index
    usecount[nr] += 1
    newnr = nr

for x in range(len(data), 30000000):
    lastnr = newnr
    newnr = 0 if usecount[lastnr] == 0 else (x-1) - lastuse[lastnr]
    lastuse[lastnr] = x - 1
    usecount[lastnr] += 1

print("Part 2: " + str(newnr))

end = time.time()
print(end - start)