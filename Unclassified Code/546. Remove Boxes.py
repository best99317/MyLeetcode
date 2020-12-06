def removeBoxes(boxes: list) -> int:
    nums = len(boxes)
    if nums == 0: return 0
    dp = [[[0] * nums for j in range(nums)] for i in range(nums)]

    def helper(l, r, k):
        if l > r: return 0
        if dp[l][r][k] != 0:
            return dp[l][r][k]
        tmp = [helper(l, i, k + 1) + helper(i + 1, r - 1, 0) for i in range(l, r) if boxes[i] == boxes[r]]
        dp[l][r][k] = max(helper(l, r - 1, 0) + (k + 1) ** 2, 0 if not tmp else max(tmp))
        return dp[l][r][k]
    return helper(0, nums - 1, 0)

boxes = [1,3,2,2,2,3,4,3,1]

print(removeBoxes(boxes))
