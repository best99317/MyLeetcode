def longestSubsequence(arr: [int], difference: int) -> int:
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[i] == arr[j] + difference:
                dp[i] = max(dp[j] + 1, dp[i])
            else:
                dp[i] = max(dp[i], 1)
    return dp[-1]
arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
difference = 0

print(longestSubsequence(arr, difference))
