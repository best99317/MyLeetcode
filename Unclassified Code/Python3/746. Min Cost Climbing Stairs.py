class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return cost[1]
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            if i == n - 1:
                dp[n - 1] = min(dp[n - 2], dp[n - 3] + cost[n - 1])
            else:
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return dp[n - 1]
