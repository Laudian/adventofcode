data = [13,16,0,12,15,1]

turns = {}
for index, nr in enumerate(data):
    turns[nr] = [index]
    lastnr = nr

for x in range(len(data), 30000000):
    if x % 100000 == 0:
        print(len(turns))
    newnr = 0 if len(turns[lastnr]) < 2 else (turns[lastnr][-1] - turns[lastnr][-2])
    turns[newnr] = [x] if newnr not in turns else turns[newnr] + [x]
    lastnr = newnr

print("Part 1: " + str(lastnr))