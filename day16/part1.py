with open("notes.txt") as file:
    notes_data = [line.strip("\n") for line in file.readlines()]

class Note(object):

    notes = []

    def __init__(self, line):
        self.name, ranges = line.split(": ")
        range1, range2 = ranges.split(" or ")
        start, end = range1.split("-")
        self.range1 = range(int(start), int(end)+1)
        start, end = range2.split("-")
        self.range2 = range(int(start), int(end)+1)
        Note.notes.append(self)

    def __contains__(self, item):
        return item in self.range1 or item in self.range2

    def isValid(nr):
        for note in Note.notes:
            if nr in note: return True
        return False


[Note(line) for line in notes_data]

with open("tickets.txt") as file:
    tickets = [line.strip("\n").split(",") for line in file.readlines()]

invalid = 0
invalid_tickets = []

for ticket in tickets:
    for nr in ticket:
        nr = int(nr)
        if not Note.isValid(nr):
            invalid += nr
            if not ticket in invalid_tickets:
                invalid_tickets.append(ticket)


print("Part1 : " + str(invalid))

# Part 2

valid_tickets = [ticket for ticket in tickets if ticket not in invalid_tickets]

ticketfields = {}
possible_fits = {}

for n in range(len(tickets[0])):
    ticketfields[n] = []

for ticket in valid_tickets:
    for index, value in enumerate(ticket):
        ticketfields[index].append(int(value))

fields = len(ticketfields)
nrs_per_field = len(ticketfields[0])

for x in range(fields):
    possible_fits[x] = []

for index, note in enumerate(Note.notes):
    for field in possible_fits:
        possible = True
        for nr in ticketfields[field]:
            if nr not in note:
                possible = False
                break
        if possible: possible_fits[index].append(field)


fits = [(x, possible_fits[x]) for x in possible_fits]

fits.sort(key=lambda x: len(x[1]))

used = []
mydict = {}

for nr, fit in fits:
    target = [x for x in fit if x not in used][0]
    used.append(target)
    mydict[nr] = target

myticket = [101,179,193,103,53,89,181,139,137,97,61,71,197,59,67,173,199,211,191,131]

result = 1

for index, note in enumerate(Note.notes):
    if note.name.startswith("departure"):
        result *= myticket[mydict[index]]

print("Part 2: " + str(result))