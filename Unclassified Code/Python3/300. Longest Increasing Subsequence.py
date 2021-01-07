def lengthOfLIS(nums: [int]) -> int:
    n = len(nums)
    if n == 0 or n == 1:
        return n
    dp = [1] * n
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [1,2,4,3,5,4,7,2]

print(lengthOfLIS(nums))
