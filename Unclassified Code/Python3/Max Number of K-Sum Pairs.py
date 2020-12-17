def maxOperations(nums: [int], k: int) -> int:
    from collections import Counter
    count = Counter(nums)
    sorted(count)
    res = 0
    for c in count:
        if k % 2 == 0 and c == k // 2:
                res += count[c] // 2
        elif k-c in count:
            res += min(count[c], count[k-c])
            count[k-c] = 0
    return res

nums = [1,2,3,4,5]
print(maxOperations(nums,k=5))

