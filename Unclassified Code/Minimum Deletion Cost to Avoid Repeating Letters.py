def minCost(s: str, cost: [int]) -> int:
    n = len(s)
    res = 0
    left = 10 ** 5
    right = -1
    for i in range(n):
        if i < n-1 and s[i] == s[i + 1]:
            left = min(left, i)
            res += cost[i]
            right = max(right, i + 1)
        else:
            if 0 <= left < n and 0 <= right < n:
                res += cost[right]
                res -= max(cost[left:right + 1])
                left = 10 ** 5
                right = -1
    return res


s = "aabaaa"
cost = [1,2,3,4,1,1]
print(minCost(s, cost))
