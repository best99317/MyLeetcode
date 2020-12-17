def getMaxLen(nums: [int]) -> int:
    length_with_neg = 0
    length_all_pos = 0
    max_length = 0
    n = len(nums)
    i = 0
    even = True
    while i < n:
        if nums[i] > 0:
            length_all_pos += 1
            length_with_neg += 1
            max_length = max(max_length, length_all_pos)
            i += 1
        elif nums[i] == 0:
            length_with_neg = 0
            even = True
            length_all_pos = 0
            i += 1
        elif nums[i] < 0:
            even = not even
            if even:
                length_with_neg += 1
                length_all_pos = length_with_neg
                max_length = max(max_length, length_with_neg)
            else:
                length_with_neg += 1
                length_all_pos = 0
            i += 1
    return max_length

nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
print(getMaxLen(nums))

