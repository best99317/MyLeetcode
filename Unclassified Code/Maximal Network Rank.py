def maximalNetworkRank(n: int, roads: [[int]]) -> int:
    dic = dict()
    if len(roads) != 0:
        for r in roads:
            if r[0] not in dic:
                dic[r[0]] = {r[1]}
            elif r[1] not in dic[r[0]]:
                dic[r[0]].add(r[1])
            if r[1] not in dic:
                dic[r[1]] = {r[0]}
            elif r[0] not in dic[r[1]]:
                dic[r[1]].add(r[0])
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            temp = len(dic[i]) if i in dic else 0
            if j in dic:
                temp += len(dic[j])
            if i in dic and j in dic[i]:
                temp -= 1
            res = max(res, temp)
    return res


n = 5
roads = [[]]

print(maximalNetworkRank(n, roads))