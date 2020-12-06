def largestDivisibleSubset(nums: [int]) -> [int]:
    if not nums: return []
    nums.sort()
    lookup = {}
    for num in nums:
        t = [num]
        for k in lookup:
            if num % k == 0 and len(lookup[k]) + 1 > len(t):
                t = lookup[k] + [num]
        lookup[num] = t

    return max(lookup.values(), key=len)
    # n = len(nums)
    # if n == 0:
    #     return []
    # nums.sort()
    # subsets = {}
    # for num in nums:
    #     if not subsets:
    #         subsets[num] = [num]
    #     else:
    #         for i in subsets:
    #             if num % subsets[i][-1] == 0:
    #                 subsets[i].append(num)
    #             else:
    #                 subsets[num] = [num]
    # return max(subsets.values(), key=len)

nums = [1,2,4,8,3,6,18,36,72]

print(largestDivisibleSubset(nums))
