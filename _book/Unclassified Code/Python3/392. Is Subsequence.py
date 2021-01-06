def isSubsequence(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)
    dp = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[i][j] = (s[i] == t[j]) if j == 0 else dp[i][j - 1] or (s[i] == t[j])
            elif j == 0:
                dp[i][j] = False
            else:
                dp[i][j] = (dp[i][j - 1] or (s[i] == t[j])) and dp[i - 1][j]

    return dp[-1][-1]


s = "abc"
t = "ahbgdc"

print(isSubsequence(s,t))
