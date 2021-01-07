def kthSmallestPath(destination: [int], k: int) -> str:
    sequence = 0

    nums = ["H"] * destination[1] + ["V"] * destination[0]
    n = destination[1] + destination[0]
    res = ""
    seen = set()
    def helper(nums: [int], ind: int, temp: [int]):
        nonlocal sequence, res, n, seen
        if res != "":
            return
        if len(temp) == n:
            temp2 = "".join(temp)
            if temp2 not in seen:
                seen.add(temp2)
                sequence += 1
                if sequence == k:
                    res = "".join(temp)
        for i in range(len(nums)):
            helper(nums[:i] + nums[i + 1:], ind + 1, temp + [nums[i]])

    helper(nums, 0, [])
    return res

destination = [15,15]
k = 155117520
print(kthSmallestPath(destination,k))