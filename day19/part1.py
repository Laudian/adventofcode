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

print(count)
print(Rule.rules["42"].getPattern())
print(Rule.rules["31"].getPattern())

# Part 2

# Rule.rules["8"].pattern = "(" + Rule.rules["42"].getPattern() + "+" + ")"
# Rule.rules["11"].pattern =