def subsets(nums: [int]) -> [[int]]:
    res = []
    n = len(nums)

    def helper(ind: int, temp: [int]):
        res.append(temp)
        for i in range(ind,n):
            helper(i + 1, temp + [nums[i]])

    helper(0, [])
    return res

nums = [1,2,3]
print(subsets(nums))