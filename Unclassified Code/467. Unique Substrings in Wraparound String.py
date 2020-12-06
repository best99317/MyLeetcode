def findSubstringInWraproundString(p: str) -> int:
    n = len(p)
    dp = [0] * n
    bow = [p[0]]
    dp[0] = 1
    for i in range(1, n):
        if p[i] not in bow:
            bow.append(p[i])
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i-1]
        for j in range(1, i + 1):
            if ord(p[i]) % 26 == (ord(p[i - j]) + j) % 26 and p[i-j:] not in bow:
                dp[i] += 1
                bow.append(p[i-j:i+1])
    return dp[-1]


p = "cabdyzab"
print(findSubstringInWraproundString(p))
