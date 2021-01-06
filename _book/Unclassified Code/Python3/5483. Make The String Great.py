def makeGood(s: str) -> str:
    n = len(s)
    res = ""
    for i in range(n):
        if len(res) == 0:
            res += s[i]
        elif ord(res[-1]) == ord(s[i]) + 32:
            res = res[:-1]
        else:
            res += s[i]
    return res

s = "abBAcC"

print(makeGood(s))
