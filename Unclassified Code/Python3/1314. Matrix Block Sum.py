def matrixBlockSum(mat: [[int]], K: int) -> [[int]]:
    m = len(mat)
    n = len(mat[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = [[0] * n for _ in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

    def getInd(i, j):
        i = min(max(i, 0), m)
        j = min(max(j, 0), n)
        return dp[i][j]

    for i in range(m):
        for j in range(n):
            res[i][j] = getInd(i + K + 1, j + K + 1) - getInd(i + K + 1, j - K) - getInd(i - K, j + K + 1) + getInd(
                i - K, j - K)
    return res