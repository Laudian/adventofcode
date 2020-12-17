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


# Create the Notes from input
[Note(line) for line in notes_data]

with open("tickets.txt") as file:
    tickets = [line.strip("\n").split(",") for line in file.readlines()]


# Find the invalid tickets

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

# find the valid tickets by removing the invalid tickets
valid_tickets = [ticket for ticket in tickets if ticket not in invalid_tickets]

fields = len(tickets[0])

ticketfields = {n : [] for n in range(fields)}  # contains the input vertically instead of horizontally
possible_fits = {n : [] for n in range(fields)}  # maps Note to the fields that fit the note

# Reordering the input
for ticket in valid_tickets:
    for index, value in enumerate(ticket):
        ticketfields[index].append(int(value))

# Check Note against each field to find possible combinations
for index, note in enumerate(Note.notes):
    for field in possible_fits:
        possible = True
        for nr in ticketfields[field]:
            if nr not in note:
                possible = False
                break
        if possible: possible_fits[index].append(field)

# Turn possible combinations into a list of (key, value) pairs
fits = [(x, possible_fits[x]) for x in possible_fits]

# Sort by length of value (meaning possible fits)
fits.sort(key=lambda x: len(x[1]))

used = [] # fields that have already been assigned to a Note
relations = {} # stores the definite Note : field relations

for nr, fit in fits:
    target = [x for x in fit if x not in used][0]
    used.append(target)
    relations[nr] = target

for fit in fits:
    print(fit)

myticket = [101,179,193,103,53,89,181,139,137,97,61,71,197,59,67,173,199,211,191,131]

result = 1

for index, note in enumerate(Note.notes):
    if note.name.startswith("departure"):
        result *= myticket[relations[index]]

print("Part 2: " + str(result))