from collections import namedtuple
from itertools import permutations


Signal = namedtuple("Signal", ["all", "output"])
letters = "abcdefg"


def convert(string, mapping):
    return "".join(sorted([mapping[letter] for letter in string]))


def process(signal: Signal, mappings):
    for mapping in mappings:
        for element in signal.all:
            mapped = convert(element, mapping)
            if mapped not in numbers:
                break
        else:
            string = [numbers[convert(nr, mapping)] for nr in signal.output]
            value = int("".join(string))
            return value

numbers = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}

with open("input.txt") as file:
    raw_data = [line.strip() for line in file]
    data = []
    for line in raw_data:
        left, right = [tuple(element) for element in [part.split() for part in line.split(" | ")]]
        all_signals = left + right
        element = Signal(all=all_signals, output=right)
        data.append(element)

mappings = []
for permutation in permutations(letters):
    mapping = dict()
    for index, letter in enumerate(letters):
        mapping[letter] = permutation[index]
    mappings.append(mapping)

count = 0
for element in data:
    count += process(element, mappings)

print("Part 2: " + str(count))
