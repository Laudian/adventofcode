with open("input.txt") as file:
    puzzle = [int(x) for x in file.read().split(",")]

max_timer = 8
cycle = 6


def simulate(steps: int):
    fish = [0]*(max_timer+1)
    for nr in puzzle:
        fish[nr] += 1

    for n in range(steps):
        fish.append(fish.pop(0))
        fish[cycle] += fish[-1]

    print(f"Fish after {steps:>3} days: " + str(sum(fish)))

simulate(80)
simulate(256)
