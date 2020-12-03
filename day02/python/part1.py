with open("../input02.txt") as file:
    data = [line.split() for line in file.readlines()]

class PasswordPolicyPair(object):
    def __init__(self, min, max, letter, password):
        self.min = int(min)
        self.max = int(max)
        self.letter = letter
        self.password = password

    def isValid(self):
        count = self.password.count(self.letter)
        return ((self.min <= count <= self.max))

    def isValid2(self):
        string = self.password[self.min-1]+self.password[self.max-1]
        return string.count(self.letter) == 1

    def __repr__(self):
        return str(self.min) + " " + str(self.max) + " " + self.letter + " " + self.password + " " + str(self.isValid())

for index, line in enumerate(data):
    min, max = line[0].split("-")
    letter = line[1].strip(":")
    password = line[2]
    data[index] = PasswordPolicyPair(min, max, letter, password)

counter = 0
counter2 = 0
for value in data:
    counter += value.isValid()
    counter2 += value.isValid2()

print("Part 1: " + str(counter))
print("Part 2: " + str(counter2))