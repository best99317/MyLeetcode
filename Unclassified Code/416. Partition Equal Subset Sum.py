def canPartition(nums: [int]) -> bool:
    if sum(nums) % 2:
        return False
    val = int(sum(nums) / 2)
    n = len(nums)
    dp = [[False] * val for _ in range(n)]
    for i in range(n):
        for j in range(val):
            if j + 1 == nums[i]:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j] if j >= nums[i] else dp[i - 1][j]
    return dp[-1][-1]


nums = [1,2,5]

print(canPartition(nums))
