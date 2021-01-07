def minimumOneBitOperations(n: int) -> int:
    # dp = [0] * (n + 1)
    # dp[1] = 1
    # time = 1
    # for i in range(2, n + 1):
    #     if i == 2 ** (time+1):
    #         time += 1
    #     dp[i] = 2 ** (time + 1) - 1 - dp[i % (2 ** (time))]
    # return dp[-1]
    b = '{0:b}'.format(n)
    digit_num = len(b)
    res = 0
    sign = 1
    for i in range(digit_num):
        if b[i] == '1':
            res += sign * 2 ** (digit_num - i)
            sign *= -1
    if sign < 0:
        res -= 1
    return res

n = 24
print(minimumOneBitOperations(n))