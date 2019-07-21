def checkBraces(string1):
    bracket_map = {'[': ']', '{': '}', '(': ')'}
    stack = []
    for bracket in string1:
        if bracket in bracket_map:
            stack.append(bracket_map[bracket])
        elif not stack or bracket != stack.pop():
            return False
    return not stack
print(checkBraces("{()}"))