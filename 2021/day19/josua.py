# puzzle input
with open("input_josua.txt") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
# with open("test input") as file:
#     testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    rules = {}
    messages = []
    rules_done = False
    for line in data:
        if line == "":
            rules_done = True
        elif rules_done:
            messages.append(line.replace("a", "99 ").replace("b", "36 "))
        else:
            rule = line.split(": ")
            rule_nr = rule[0] + " "
            subrules = rule[1].split("| ")
            for subrule in subrules:
                if not subrule.endswith(" "):
                    subrule = subrule + " "
                if tuple(subrule) not in rules.keys():
                    rules[tuple(subrule)] = [rule_nr]
                else:
                    rules[tuple(subrule)].append(rule_nr)
    return rules, messages


def checkIfValid(message, rules):
    global counter
    message_list = list(message)
    for index, letter in enumerate(message_list):
        if letter == "a":
            message_list[index] = "99"
        else:
            message_list[index] = "36"
    done = False
    results = [message_list]
    valid = False
    while not done:
        new_results = []
        for result in results:
            combinations = [x for x in result if x in ("36", "42", "99")]
            for index in range(0, len(result)-2):
                combinations.append((result[index], result[index+1]))

            for key in rules.keys():
                if len(key) == 1:
                    if key in result:
                        index = result.index(key)
                        result_copy = result.copy()
                        result_copy[index] = rules[key]
                        if result_copy not in results:
                            new_results.append(result_copy)
                else:
                    try:
                        index0 = result.index(key[0])
                        if result[index0+1] == key[1]:
                            counter += 1
                            if counter % 10000 == 0:
                                print(counter)
                            for rule_nr in rules[key]:
                                result_copy = result.copy()
                                result_copy[index0] = rule_nr
                                result_copy.pop(index0+1)
                                if result_copy not in results:
                                    new_results.append(result_copy)
                    except (ValueError, IndexError):
                        pass
        results = new_results.copy()
        if not results:
            done = True
        if ["0"] in results:
            done = True
            valid = True
    return valid


def validateMessages(messages, rules):
    count = 0
    for message in messages:
        valid = checkIfValid(message, rules)
        print(valid)
        if valid:
            count += 1
    return count


rules, messages = formatData(rawdata)
counter = 0
print(rules)
print(validateMessages(messages, rules))