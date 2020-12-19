import re

class Rule(object):
    rules = {}

    def __init__(self, name, target):
        if target == "\"a\"":
            self.pattern = "a"
            self.has_pattern = True
        elif target == "\"b\"":
            self.pattern = "b"
            self.has_pattern = True
        else:
            self.target = target
            self.has_pattern = False
        Rule.rules[name] = self

    def getPattern(self):
        if self.has_pattern:
            return self.pattern
        else:
            # Split target into alternatives
            alternatives = self.target.split(" | ")

            # retrieve pattern of each alternative and append or if it is not the last
            pattern = ["("]
            for index, alternative in enumerate(alternatives):
                # pattern.append("(")
                rules = alternative.split(" ")
                for rule in rules:
                    pattern.append(Rule.rules[rule].getPattern())
                # pattern.append(")")
                if index != len(alternatives)-1:
                    pattern.append("|")
            pattern.append(")")
            self.pattern = "".join(pattern)
            self.has_pattern = True
            return self.pattern

with open("rules.txt") as file:
    data = [line.strip("\n").split(": ") for line in file]

for line in data:
    Rule(line[0], line[1])

with open("messages.txt") as file:
    messages = [line for line in file]

count = 0
for message in messages:
    if re.match("^" + Rule.rules["0"].getPattern() + "$", message) is not None:
        count += 1

print("Part 1: " + str(count))

# Part 2

def matchEnd(end, max_matches):
    pattern = "^" + Rule.rules["31"].getPattern() + "{1," + str(max_matches) + "}" + "$"
    return False if re.match(pattern, end) is None else True

# Since every repetition of rule 42 adds at least one character, it can repeat no more than this
upper_limit = len(max(messages)) / 4

def match(string):
    n = 2 # Rule 8 matches 42 at least once, rule 11 matches 42 at least once which means at least 2 matches
    while n <= upper_limit:
        pattern = "^" + n * Rule.rules["42"].getPattern()
        partial_match = re.match(pattern, string)
        if partial_match is not None:
            end = string[partial_match.span()[1]:]
            if matchEnd(end, n-1):
                return True
        n += 1
    return False

count = 0
for message in messages:
    if match(message):
        count += 1

print("Part 2: " + str(count))