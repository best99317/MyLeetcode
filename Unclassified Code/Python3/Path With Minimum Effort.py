def minimumEffortPath(heights: [[int]]) -> int:
    m = len(heights)
    n = len(heights[0])
    if m == 1 and n == 1:
        return 0
    queue = [(0, 0, 0)]
    visited = {(0, 0)}
    while queue:
        i, j, cost = queue.pop(0)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= i + dx < n and 0 <= j + dy < n and (i + dx, j + dy) not in visited:
                queue.append((i + dx, j + dy, max(cost, abs(heights[i + dx][j + dy] - heights[i][j]))))
                visited.add((i + dx, j + dy))  # mark as visited
        if i + dx == n - 1 and j + dy == n - 1:
            break
    return cost

heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPath(heights))
