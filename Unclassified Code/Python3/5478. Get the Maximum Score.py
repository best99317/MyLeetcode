def maxSum(nums1, nums2) -> int:
    m = len(nums1)
    n = len(nums2)
    dp1 = [0] * (m+1)
    dp2 = [0] * (n+1)

    i = 0
    j = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            dp1[i+1] = dp1[i] + nums1[i]
            i += 1
        elif nums1[i] > nums2[j]:
            dp2[j+1] += dp2[j] + nums2[j]
            j += 1
        else:
            dp1[i + 1] = max(dp1[i], dp2[j]) + nums1[i]
            dp2[j + 1] += max(dp1[i], dp2[j]) + nums2[j]
            i += 1
            j += 1

    while i < m:
        dp1[i + 1] = dp1[i] + nums1[i]
        i += 1
    while j < n:
        dp2[j + 1] += dp2[j] + nums2[j]
        j += 1

    return max(dp1[m], dp2[n])

a1 = [2,4,5,8,10]
a2 = [4,6,8,9]

res = maxSum(a1,a2)
print(res)