def permute(nums: [int]) -> [[int]]:
    res = list()
    n = len(nums)

    def helper(nums: [int], ind: int, temp: [int]):
        if len(temp) == n:
            res.append(temp)
        for i in range(len(nums)):
            helper(nums[:i] + nums[i+1:], ind+1, temp + [nums[i]])

    helper(nums,0,[])
    return res

nums = [1,2,3]

print(permute(nums))
