def subsetsWithDup(nums: [int]) -> [[int]]:
    res = []
    n = len(nums)
    nums.sort()
    def helper(ind: int, temp: [int]):
        if temp not in res:
            res.append(temp)
            for i in range(ind, n):
                helper(i + 1, temp + [nums[i]])

    helper(0, [])
    return res

nums = [4,4,4,1,4]
print(subsetsWithDup(nums))
