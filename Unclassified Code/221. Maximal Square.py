def maximalSquare(matrix: [[str]]) -> int:
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(m)]
    max_l = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == '0':
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] >= max_l:
                max_l = dp[i][j]
    return max_l ** 2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(maximalSquare(matrix))
