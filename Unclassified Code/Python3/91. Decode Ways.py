def numDecodings(s: str) -> int:
    n = len(s)
    dp = [0] * n
    if int(s[0]) in range(1, 10):
        dp[0] = 1
    else:
        return 0
    if n == 1:
        return 1
    if int(s[0:2]) <= 26 and s[1] != '0':
        dp[1] = 2
    elif int(s[0:2]) <= 26:
        dp[1] = 1
    elif s[1] == '0':
        return 0
    else:
        dp[1] = 1

    for i in range(2, n):
        if s[i] == '0' and (s[i - 1] == '1' or s[i - 1] == '2'):
            dp[i] = dp[i - 2]
        elif s[i] != '0':
            if int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        else:
            return 0
    return dp[n - 1]


s = "227"
print(numDecodings(s))
