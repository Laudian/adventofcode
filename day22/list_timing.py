import timeit

def play(hands):
    configurations = set()
    while hands[0] and hands[1]:
        # Check if configuration is new, else player 0 wins
        configuration = (tuple(hands[0]), tuple(hands[1]))
        if configuration in configurations:
            return 0
        # Each player draws his first card
        cards = hands[0].pop(0), hands[1].pop(0)
        # Check if both players have as many cards as the value they've just drawn left
        if (len(hands[0]) < cards[0]) or (len(hands[1]) < cards[1]):
            # If not, the player with the higher card wins
            winner = cards[1] > cards[0]
        else:
            # Play the game recursively on the remaining cards to determine the winner of this round
            copy1 = hands[0][0:cards[0]]
            copy2 = hands[1][0:cards[1]]
            # If player 0 has the highest card he will always win, playing recursively is not necessary
            if max(copy1) > max(copy2):
                winner = 0
            else:
                winner = play((copy1, copy2))
        # Save this configuration
        configurations.add(configuration)
        # The winner gets both cards
        hands[winner].append(cards[winner])
        hands[winner].append(cards[not winner])
    return winner

def run():
    hands = (
        [26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9],
        [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]
    )
    play(hands)

setupcode = """
from __main__ import run
"""

nr = 1000
print(timeit.timeit(stmt="run()", setup=setupcode, number=nr)/nr)