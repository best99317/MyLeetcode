def maxNonOverlapping(nums: [int], target: int) -> int:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    targets = []
    res = []
    length = []
    for i in range(n):
        for j in range(i+1):
            if i == j:
                dp[i][j] = nums[i]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + nums[i]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if dp[i][j] == target:
                targets.append([j, i])
    targets.sort()
    for i in targets:
        if len(res) == 0:
            res.append([i])
        else:
            t = len(res)
            for j in range(t):
                if res[j][-1][-1] < i[0]:
                    temp = res[j].copy()
                    temp.append(i)
                    res.append(temp)
                elif j == t-1:
                    res.append([i])
    for i in res:
        length.append(len(i))
    return max(length) if len(length) > 0 else 0

nums = [3,0,2,0,2,3,3,0,0,2,1,1,1,0,-1,-1,1,-1,1,0,2,0,0,3,0,0,3,1,0,2,0,-1,2,-1,1,1,3,0,2,3,3,0,0,2,-1,1]
target = 3

print(maxNonOverlapping(nums,target))
