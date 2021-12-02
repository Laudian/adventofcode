import time
rawdata = [0, 20, 7, 16, 1, 18, 15]
testdata = [0, 3, 6]



def playGame(starting_numbers, game_lengh):
    mentioned_numbers = {}
    for index, value in enumerate(starting_numbers[:-1]):
        mentioned_numbers[value] = index + 1
    starting_numbers.reverse()
    turn = len(starting_numbers)
    starting_number = starting_numbers[0]
    for i in range(turn + 1, game_lengh + 1, 1):
        if starting_number not in mentioned_numbers.keys():
            mentioned_numbers[starting_number] = i - 1
            starting_number = 0
        else:
            new_number = i - 1 - mentioned_numbers[starting_number]
            mentioned_numbers[starting_number] = i - 1
            starting_number = new_number
    return starting_number

start = time.time()
print(playGame(rawdata, 30000000))
end = time.time()
print(end - start)