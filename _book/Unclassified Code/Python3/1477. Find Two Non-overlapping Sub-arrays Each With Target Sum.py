def minSumOfLengths(arr: [int], target: int) -> int:
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    targets = []
    length = []
    res = []
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                dp[i][j] = arr[i]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + arr[i]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if dp[i][j] == target:
                targets.append([j, i])
    for i in targets:
        if len(res) == 0:
            res.append([i])
        else:
            t = len(res)
            for j in range(t):
                if res[j][-1][-1] < i[0] and len(res[j]) < 2:
                    temp = res[j].copy()
                    temp.append(i)
                    res.append(temp)
                elif j == t-1:
                    res.append([i])
    for i in res:
        if len(i) == 2:
            length.append(i[0][1]-i[0][0] + i[1][1] - i[1][0] + 2)
    return min(length) if len(length) > 0 else -1

arr = [10,36,1,8,1,27,3,9,16,1,48,5,2,1,36,20,11,43,2,28,12,3,7,1,5,22,27,6,1,17,13,9,14,2,1,32,23,1,28,27,1,39,17,44,10,2,1,36,19,24,23,5,4,18,34,1,1,1,1,51,1,4,50,3,2,1,7,1,15,30,2,1,40,13,2,1,56,47,3,4,2,52,1,3,4,45,7,13,3,13,11,15,1,33,8,14,1,48,7,1,15,31,4,2,3,1,22,25,2,3,1,3,11,44,1,53,1,2,42,13,1,11,35,3,2,3,1,1,34,16,6,18,6,27,2,2,1,10,17,25,2,1,1,32,22,1,1,37,9,6,3,1,37,13,5,1,37,13,5,1,39,6,10,1,21,8,11,9,7,34,11,4,5,1,1,17,12,25,1,1,32,7,9,7,1,15,31,1,8,1,21,13,7,9,1,4,1,32,20,3,1,44,7,1,1,2,1,36,12,4,4,7,47,1,1,22,13,6,10,2,2]
target = 56

print(minSumOfLengths(arr,target))
