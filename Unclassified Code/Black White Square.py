def paintingPlan(n: int, k: int) -> int:
    if k == 0:
        return 1
    if k < n:
        return 0
    if k == n * n:
        return 1
    board = [[0] * n for _ in range(n)]
    res = 0

    def helper(board, row_ind, col_ind, row, col):
        nonlocal res
        cur_sum = sum([sum(i) for i in board])
        if cur_sum == k:
            res += 1
            return
        elif cur_sum > k:
            return
        if row_ind >= n or col_ind >= n:
            return
        if row:
            for i in range(n):
                board[row_ind][i] = 1
        if col:
            for j in range(n):
                board[j][col_ind] = 1
        helper(board, row_ind + 1, col_ind, True, False)
        helper(board, row_ind, col_ind + 1, False, True)
        helper(board, row_ind + 1, col_ind + 1, True, True)

    for i in range(n):
        for j in range(n):
            helper(board, i, j, True, False)
            helper(board, i, j, False, True)
            helper(board, i, j, True, True)
    return res


n = 2
k = 2
print(paintingPlan(n,k))

