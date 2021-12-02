import timeit

class cupgame(object):
    cups = {}

    def __init__(self, value):
        self.nr = value
        cupgame.cups[self.nr] = self

    def __repr__(self):
        return repr(self.nr)

    @classmethod
    def removeNextThree(cls):
        cls.removed_start = cls.current.next
        cls.removed_end = cls.removed_start.next.next
        cls.current.next = cls.removed_end.next
        cls.removedCups = (cls.removed_start.nr, cls.removed_start.next.nr, cls.removed_end.nr)
        return

    @classmethod
    def insertRemoved(cls, dest):
        cls.removed_end.next = dest.next
        dest.next = cls.removed_start
        return

    @classmethod
    def play(cls, rounds=1):
        for x in range(rounds):
            cls.removeNextThree()
            dest = cls.current.getDestination()
            cls.insertRemoved(dest)
            cls.current = cls.current.next

    def getDestination(self):
        dest = (self.nr - 1) if self.nr > 1 else len(cupgame.cups)
        while dest in cupgame.removedCups:
            dest = (dest - 1) if dest > 1 else len(cupgame.cups)
        return cupgame.cups[dest]

def run():
    data = [4, 9, 6, 1, 3, 8, 5, 2, 7]

    all = list(range(1, 1000001))
    for index, value in enumerate(data):
        all[index] = value

    for index, value in enumerate(all):
        next = cupgame(value)
        if index:
            cupgame.cups[all[index - 1]].next = next

    cupgame.current = cupgame.cups[data[0]]
    next.next = cupgame.current

    cupgame.play(rounds=10000000)

    print(cupgame.cups[1].next.nr*cupgame.cups[1].next.next.nr)

print(timeit.timeit(stmt="run()", setup="from __main__ import run", number=1))