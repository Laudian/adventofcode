from collections import deque
from itertools import islice
import timeit

def calcScore(hand):
    score = 0
    for index, card in enumerate(reversed(hand), 1):
        score += card * index
    return score

def setup():
    global hands
    # hands = (
    #          deque([44, 24, 36, 6, 27, 46, 33, 45, 47, 41, 15, 23, 40, 38, 43, 42, 25, 5, 30, 35, 34, 13, 29, 1, 50]),
    #          deque([32, 28, 4, 12, 9, 21, 48, 18, 31, 39, 20, 16, 3, 37, 49, 7, 17, 22, 8, 26, 2, 14, 11, 19, 10])
    #         )
    hands = (
        deque([26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9]),
        deque([27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34])
    )

def run_part1():
    setup()
    while hands[0] and hands[1]:
        cards = hands[0].popleft(), hands[1].popleft()
        winner = cards[1] > cards[0]
        hands[winner].append(cards[winner])
        hands[winner].append(cards[not winner])

def play_part2(hands):
    global all_configs
    configurations = {}
    while hands[0] and hands[1]:
        # Check if configuration is new
        configuration = (tuple(hands[0]), tuple(hands[1]))
        if configuration in configurations:
            print(len(configurations))
            return 0
        # elif configuration in all_configs:
        #     return all_configs[configuration]
        cards = hands[0].popleft(), hands[1].popleft()
        # Check if both players have enough cards left
        if (len(hands[0]) < cards[0]) or (len(hands[1]) < cards[1]):
            winner = cards[1] > cards[0]
        else:
            copy1 = deque(islice(hands[0], 0, cards[0]))
            copy2 = deque(islice(hands[1], 0, cards[1]))
            if max(copy1) > max(copy2):
                winner = 0
            else:
                winner = play_part2((copy1, copy2))
        configurations[configuration] = winner
        # all_configs[configuration] = all_configs.get(configuration, 0) + 1
        hands[winner].append(cards[winner])
        hands[winner].append(cards[not winner])
    return winner

def run_part2():
    setup()
    winner = play_part2(hands)
    print(calcScore(hands[winner]))

setupcode = """
from __main__ import run_part1
from __main__ import run_part2
"""

nr = 1
# print(timeit.timeit(stmt="print(run_part1())", setup=setupcode, number=nr))
print(timeit.timeit(stmt="run_part2()", setup=setupcode, number=nr))