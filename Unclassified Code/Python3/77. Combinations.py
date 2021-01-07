def combine(n: int, k: int) -> [[int]]:
    res = list()

    def helper(ind: int, temp: [int]):
        if len(temp) == k:
            res.append(temp)
            return
        for i in range(ind, n):
            helper(i + 1, temp + [i + 1])

    helper(0, [])
    return res

n = 4
k = 2

print(combine(n,k))
