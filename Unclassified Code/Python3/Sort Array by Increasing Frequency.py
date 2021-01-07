def frequencySort(nums: [int]) -> [int]:
    n = len(nums)
    dic1 = {}
    for i in range(n):
        if nums[i] not in dic1:
            dic1[nums[i]] = 1
        else:
            dic1[nums[i]] += 1
    dic2 = {}
    for i in dic1:
        if dic1[i] not in dic2:
            dic2[dic1[i]] = [i]
        else:
            dic2[dic1[i]].append(i)
            dic2[dic1[i]].sort(reverse=True)
    arranged = set()
    dic1 = {k: v for k, v in sorted(dic1.items(), key=lambda item: item[1])}
    res = list()
    for i in dic1:
        if i not in arranged:
            if len(dic2[dic1[i]]) > 1:
                for j in dic2[dic1[i]]:
                    res += [j] * dic1[j]
                    arranged.add(j)
            else:
                res += [i] * dic1[i]
                arranged.add(i)
    return res

nums = [-1,1,-6,4,5,-6,1,4,1]

print(frequencySort(nums))