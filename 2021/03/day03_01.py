with open("input.txt") as file:
    puzzle = [line.strip("\n") for line in file.readlines()]


def transpose(iterable):
    return list(zip(*iterable))


def gamma_epsilon(puzzle):
    gamma, epsilon = [], []
    puzzle_transposed = transpose(puzzle
                                  )
    for sequence in puzzle_transposed:
        one_count = sequence.count("1")
        zero_count = sequence.count("0")

        gamma.append("1" if (flag := one_count > zero_count) else "0")
        epsilon.append("0" if flag else "1")

    gamma_value = int("".join(gamma), 2)
    epsilon_value = int("".join(epsilon), 2)
    return gamma_value, epsilon_value


def filter_rating(puzzle, oxygen=True):
    copy = list(puzzle)
    index = 0

    while len(copy) > 1:
        new_copy = []
        copy_transposed = transpose(copy)
        one_count = copy_transposed[index].count("1")
        zero_count = copy_transposed[index].count("0")

        if oxygen:
            bit = "1" if one_count >= zero_count else "0"
        else:
            bit = "1" if one_count < zero_count else "0"

        for sequence in copy:
            if sequence[index] == bit:
                new_copy.append(sequence)

        copy = new_copy
        index += 1

    return int("".join(copy[0]), 2)

gamma, epsilon = gamma_epsilon(puzzle)
print("Part 1: " + str(gamma * epsilon))

oxygen = filter_rating(puzzle)
co2 = filter_rating(puzzle, oxygen=False)

print("Part 2: " + str(oxygen*co2))