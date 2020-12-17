def canConvertString(s: str, t: str, k: int) -> bool:
    m = len(s)
    n = len(t)
    if m != n:
        return False
    op = [i for i in range(27)]
    for i in range(m):
        dist = (ord(t[i]) - ord(s[i])) % 26
        if op[dist] > k:
            return False
        elif dist != 0:
            op[dist] += 26
    return True

s = 'aab'
t = 'bbb'
k = 27
print(canConvertString(s,t,k))
