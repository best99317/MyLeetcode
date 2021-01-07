class NumMatrix:

    def __init__(self, matrix: [[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] + self.dp[row1][col1] - self.dp[row1][col2+1] - self.dp[row2+1][col1]


matrix = [[3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]

A = NumMatrix(matrix)
print(A.sumRegion(2,1,4,3))
