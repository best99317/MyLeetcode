def containsCycle(grid: [[str]]) -> bool:
    m = len(grid)
    n = len(grid[0])
    stack = list()
    past = list()
    for i in range(m):
        for j in range(n):
            stack.append([i, j])
            past.append([i, j])
            while stack:
                pos = stack.pop()
                for di in (-1, 1):
                    if 0 <= i + di < m:
                        if grid[pos[0] + di][pos[1]] == grid[pos[0]][pos[1]]:
                            if [pos[0] + di, pos[1]] in past:
                                return True
                            else:
                                stack.append([pos[0] + di, pos[1]])
                                past.append([pos[0] + di, pos[1]])
                for dj in (-1, 1):
                    if 0 <= pos[1] + dj < n:
                        if grid[pos[0]][pos[1] + dj] == grid[pos[0]][pos[1]]:
                            if [pos[0], pos[1] + dj] in past:
                                return True
                            else:
                                stack.append([pos[0], pos[1] + dj])
                                past.append([pos[0], pos[1]+dj])
            past = []
    return False

grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
print(containsCycle(grid))
