def maxUniqueSplit(s: str) -> int:
    n = len(s)
    res = 0

    def helper(temp, ind):
        nonlocal res
        if ind >= n:
            res = max(res, len(temp))
            return
        for i in range(ind, n):
            if s[ind:i + 1] not in temp:
                helper(temp+[s[ind:i + 1]], i + 1)

    helper([], 0)
    return res

s = "ababccc"
print(maxUniqueSplit(s))