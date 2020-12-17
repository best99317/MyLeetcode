def mincostTickets(days: [int], costs: [int]) -> int:
    n = len(days)
    if n == 0:
        return 0
    if n == 1:
        return costs[0]
    dp = [365 * 1000] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + costs[0], dp[i])
        for j in range(1, i + 1):
            if days[i - 1] - days[i - j] < 7:
                dp[i] = min(dp[i - j] + costs[1], dp[i])
            if days[i - 1] - days[i - j] < 30:
                dp[i] = min(dp[i - j] + costs[2], dp[i])
    return dp[-1]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

print(mincostTickets(days, costs))
