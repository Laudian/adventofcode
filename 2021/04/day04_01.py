from itertools import chain


class BingoCard(object):
    def __init__(self, rows):
        self.fields = list(chain(*rows))
        self.sidelength = len(rows[0])
        self.size = len(self.fields)
        self.finished = False

    def mark(self, nr):
        if self.finished:
            return False
        for index, value in enumerate(self.fields):
            if value == nr:
                self.fields[index] = "x"
                return self.check_winner()
        return False

    def check_winner(self):
        for x in range(5):
            # Check row
            row_offset = 5*x
            row_count = self.fields[0+row_offset:self.sidelength+row_offset].count("x")

            # Check column
            column_count = self.fields[x:self.size:self.sidelength].count("x")

            if row_count == self.sidelength or column_count == self.sidelength:
                self.finished = True
                return self.calculate_score()
        return False

    def calculate_score(self):
        score = sum(filter(lambda f: f != "x", self.fields))
        return score

with open("input.txt") as file:
    numbers = [int(x) for x in file.readline().split(",")]
    puzzle = [[int(x) for x in line.strip().split()] for line in file if line != "\n"]

cards = []
while len(puzzle) > 0:
    card = BingoCard(puzzle[0:5])
    cards.append(card)
    puzzle = puzzle[5:]

part1 = True
for nr in numbers:
    for card in cards:
        if score := card.mark(nr):
            if part1:
                winner_score = score*nr
                part1 = False
            else:
                loser_score = score*nr

# noinspection PyUnboundLocalVariable
print("Part 1: " + str(winner_score))
# noinspection PyUnboundLocalVariable
print("Part 2: " + str(loser_score))
