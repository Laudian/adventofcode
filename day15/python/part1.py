import time
import itertools

data = [13,16,0,12,15,1]

start = time.time()

lastuse = list(itertools.repeat([], 30000000))
usecount = [0] * 30000000

print(time.time() - start)

for index, nr in enumerate(data):
    lastuse[nr] += [index]
    usecount[nr] += 1
    lastnr = nr

for x in range(len(data), 30000000):
    lastnr = 0 if usecount[lastnr] < 2 else (x - 1) - lastuse[lastnr][-2]
    lastuse[lastnr] += [x]
    usecount[lastnr] += 1

print("Part 1: " + str(lastnr))

end = time.time()
print(end - start)