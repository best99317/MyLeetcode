def countBits(num: int) -> [int]:
    dp = [0] * (num + 1)
    count = 1
    for i in range(1, num + 1):
        dp[i] = dp[i - count] + 1
        if i == count * 2 - 1:
            count *= 2
    return dp

num = 15

print(countBits(num))
