def findNumberOfLIS(nums: [int]) -> int:
    n = len(nums)
    if n == 0 or n == 1:
        return n
    dp = [1] * n
    count = [0] * n
    count[0] = 1
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] == dp[i - 1] + 1:
                    count[i] += 1

    return count[-1]
nums = [1,2,4,3,5,4,7,2]

print(findNumberOfLIS(nums))