def containsPattern(arr: [int], m: int, k: int) -> bool:
    n = len(arr)
    res = False
    max_count = 0
    for i in range(n - m):
        pattern = arr[i:i + m]
        count = 1
        j = i + m
        while j + m <= n:
            if arr[j:j + m] == pattern:
                count += 1
                j = j + m
            else:
                break
        max_count = max(count, max_count)
    if max_count >= k:
        res = True
    return res

arr = [1,2,3,1,2]
m = 2
k = 2
print(containsPattern(arr, m, k))