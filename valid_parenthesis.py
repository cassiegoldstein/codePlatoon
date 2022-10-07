def isValid(s):
    stack = []
    dict_lookup = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for parenthesis in s:
        if parenthesis in dict_lookup.values():
            stack.append(parenthesis)
        elif stack and dict_lookup[parenthesis] == stack[-1]:
            stack.pop()
        else: 
            return False
    if stack == []:
        return True
    else: 
        return False

s = "()[}"
print(isValid(s))
