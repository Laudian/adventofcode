with open("input.txt") as file:
    data = [line.strip("\n").replace(" ", "") for line in file]

operators =\
    {
        "*": (lambda left, right: left * right),
        "+": (lambda left, right: left + right)
    }

def splitExpression(expression):
    char = expression[-1]
    # If char is a closing bracket, search for the corresponding opening bracket
    if char == ")":
        level = -1
        index = -1
        while level != 0:
            index -= 1
            char = expression[index]
            if char == "(":
                level += 1
            elif char == ")":
                level -= 1

        right = expression[index+1:-1]
        left = expression[:index]
    else:
        right = expression[-1]
        left = expression[:-1]
    return left, right



def parseExpression(expression):
    # Parse expression with recursive descent from right to left

    # Default case: only 1 char left
    if len(expression) == 1:
        return int(expression)

    # Split the expression
    left, right = splitExpression(expression)
    right = parseExpression(right)

    if left:
        operator = left[-1]
        left = parseExpression(left[:-1])
        result = operators[operator](left, right)
        return result
    return right

result = 0
for expression in data:
    result += parseExpression(expression)
print("Part1: " + str(result))