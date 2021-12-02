public_door, public_card = 1526110, 20175123
# public_door, public_card = 17807724, 5764801

def findLoopSize(subject, target):
    value = 1
    loops = 0
    while value != target:
        value = (value * subject) % 20201227
        loops += 1
    return loops

def transform(subject, loopsize):
    value = 1
    for n in range(loopsize):
        value = (value * subject) % 20201227
    return value

print(transform(public_card, findLoopSize(7, public_door)))

