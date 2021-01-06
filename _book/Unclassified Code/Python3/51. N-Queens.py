def solveNQueens(n: int) -> [[str]]:
    res = list()

    def generateRes(temp):
        ans = list()
        for ind in temp:
            ans.append("." * ind + "Q" + "." * (n - ind - 1))
        return ans

    def helper(temp):
        # check conflict
        ind = len(temp) - 1
        for i in range(ind):
            if abs(temp[-1] - temp[i]) == ind - i:
                return

        if len(temp) == n:
            res.append(generateRes(temp))
            return
        for j in [k for k in range(n) if k not in temp]:
            helper(temp+[j])

    for i in range(n):
        helper([i])
    return res


n = 5
print(solveNQueens(n))
