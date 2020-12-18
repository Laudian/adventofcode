with open("input.txt") as file:
    data = [line.strip("\n").replace(" ", "") for line in file]

def operatorAddition(left, right):
    rightvalue = right
    if len(left) == 1:
        return parseExpression(left) + rightvalue
    else:
        left, right = splitExpression(left)
        right = parseExpression(right) + rightvalue
        if left:
            operator = left[-1]
            left = left[:-1]
            result = operators[operator](left, right)
            return result
        return right

def operatorMultiplication(left, right):
    return parseExpression(left) * right


operators =\
    {
        "*": operatorMultiplication,
        "+": operatorAddition
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
        left = left[:-1]
        result = operators[operator](left, right)
        return result
    return right

result = 0
for expression in data:
    result += parseExpression(expression)
print("Part2: " + str(result))