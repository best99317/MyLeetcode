def unhappyFriends(n: int, preferences: [[int]], pairs: [[int]]) -> int:
    unhappy_num = [0] * n
    for i in range(n // 2):
        for j in [k for k in range(i)] + [k for k in range(i + 1, n // 2)]:
            if (preferences[pairs[i][0]].index(pairs[j][0]) < preferences[pairs[i][0]].index(pairs[i][1]) and
                    preferences[pairs[j][0]].index(pairs[i][0]) < preferences[pairs[j][0]].index(pairs[j][1])):
                unhappy_num[pairs[i][0]] = 1
            elif (preferences[pairs[i][0]].index(pairs[j][1]) < preferences[pairs[i][0]].index(pairs[i][1]) and
                  preferences[pairs[j][1]].index(pairs[i][0]) < preferences[pairs[j][1]].index(pairs[j][0])):
                unhappy_num[pairs[i][0]] = 1
            if (preferences[pairs[i][1]].index(pairs[j][0]) < preferences[pairs[i][1]].index(pairs[i][0]) and
                    preferences[pairs[j][0]].index(pairs[i][1]) < preferences[pairs[j][0]].index(pairs[j][1])):
                unhappy_num[pairs[i][1]] = 1
            elif (preferences[pairs[i][1]].index(pairs[j][1]) < preferences[pairs[i][1]].index(pairs[i][0]) and
                  preferences[pairs[j][1]].index(pairs[i][1]) < preferences[pairs[j][1]].index(pairs[j][0])):
                unhappy_num[pairs[i][1]] = 1

    return sum(unhappy_num)


n = 6
preferences = [[1,4,3,2,5],[0,5,4,3,2],[3,0,1,5,4],[2,1,4,0,5],[2,1,0,3,5],[3,4,2,0,1]]
pairs = [[3,1],[2,0],[5,4]]

print(unhappyFriends(n, preferences, pairs))