def minInsertions(s: str) -> int:
    stack_left = []
    stack_right = []
    res = 0
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            stack_left.append(s[i])
        else:
            if len(stack_left) == 0:
                if i > 0 and len(stack_right) != 0:
                    res += 1
                    stack_right.pop()
                else:
                    stack_right.append(s[i])
            elif stack_left[-1] == '(' and len(stack_right) != 0:
                stack_left.pop()
                stack_right.pop()
            else:
                stack_right.append(s[i])
    res += 2 * len(stack_right)
    res += len(stack_left)
    return res

s = "(()))"

print(minInsertions(s))
