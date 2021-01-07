def minDays(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    if n == 1:
        return 1
    dp[2] = 2
    if n == 2:
        return 2
    for i in range(2, n + 1):
        dp[i] = min(dp[i - int(i / 2)] + 1 if i % 2 == 0 else float("inf"),
                    dp[i - int(2 * i / 3)] + 1 if i % 3 == 0 else float("inf"),
                    dp[i - 1] + 1)
    return dp[-1]
n = 56
print(minDays(n))
