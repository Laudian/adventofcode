with open("input.txt") as file:
    puzzle = [line.strip() for line in file]

target_lengths = [2, 3, 4, 7]
count = 0
for line in puzzle:
    left, right = line.split(" | ")
    output = right.split()
    for signal in output:
        count += len(signal) in target_lengths

print(count)