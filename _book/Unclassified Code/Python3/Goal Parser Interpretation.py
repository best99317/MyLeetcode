def interpret(command: str) -> str:
    stack = []
    res = ""
    for c in command:
        if c == "G":
            res += "G"
        elif c == "(" or c == "l":
            stack.append(c)
        elif c == ")":
            if stack[-1] == "(":
                res += "o"
            else:
                res += "al"
            stack = []
    return res

command= "(al)G(al)()()G"
print(interpret(command))