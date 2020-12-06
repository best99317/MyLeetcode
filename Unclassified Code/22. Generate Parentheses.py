def generateParenthesis( n: int) -> [str]:
    res = list()
    def dfs(left, right, cur):
        if left == 0 and right == 0:
            res.append(cur)
            return
        if left < 0 or right < 0 or left > right:
            return
        dfs(left - 1, right, cur + "(")
        dfs(left, right - 1, cur + ")")

    dfs(n, n, "")
    return res


n = 3
print(generateParenthesis(n))
