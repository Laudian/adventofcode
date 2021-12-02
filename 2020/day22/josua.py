import timeit

def playRecursiveCombat(player_decks):
    played_rounds = set()
    while True:
        # endless games end with player 1 winning
        saved_decks = (tuple(player_decks[0]), tuple(player_decks[1]))
        if saved_decks in played_rounds:
            return 0
        else:
            played_rounds.add(saved_decks)
        # collect cards from top of decks
        played_cards = [player_decks[0].pop(0), player_decks[1].pop(0)]
        # determine round winner via higher card
        if played_cards[0] > len(player_decks[0]) or played_cards[1] > len(player_decks[1]):
            round_winner = played_cards[1] > played_cards[0]
        # determine round winner via subgame
        else:
            subgame_decks = [player_decks[0][:played_cards[0]], player_decks[1][:played_cards[1]]]
            if max(subgame_decks[0]) > max(subgame_decks[1]):
                round_winner = 0
            else:
                round_winner = playRecursiveCombat(subgame_decks)
        # add cards to round winners deck in the right order
        if round_winner:
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        if not player_decks[0] or not player_decks[1]:
            return round_winner



def run():
    x = [[26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9],
        [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]]
    y = playRecursiveCombat(x)

setupcode = """
from __main__ import run
"""
nr = 1000
print(timeit.timeit(stmt=run, setup=setupcode, number=nr)/nr)