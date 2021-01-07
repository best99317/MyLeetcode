import math
def soupServings(N: int) -> float:
    n = math.ceil(N / 25)
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[-1][-1] = 1
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for (dA, dB) in ((-4, -0), (-3, -1), (-2, -2), (-1, -3)):
                if i + dA < n+1 and j + dB < n+1:
                    dp[max(i + dA,0)][max(j + dB,0)] += dp[i][j] / 4
    return sum(dp[0][1:]) + 0.5 * dp[0][0]

print(soupServings(50))