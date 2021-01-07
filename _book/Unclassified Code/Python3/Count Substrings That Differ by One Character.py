def countSubstrings(s: str, t: str) -> int:
    res = 0
    m = len(s)
    n = len(t)

    def comp(sub_s, sub_t):
        n = len(sub_s)
        res = 0
        for i in range(n):
            if sub_s[i] != sub_t[i]:
                res += 1
        return res == 1

    for l in range(min(m, n)):
        for i in range(m - l):
            for j in range(n - l):
                if comp(s[i:i + l + 1], t[j:j + l + 1]):
                    res += 1
    return res

s = "abe"
t = "bbc"
print(countSubstrings(s,t))