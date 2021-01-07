def findKthPositive(arr: [int], k: int) -> int:
    integer = 1
    ind = 0
    count = 0
    while count != k and ind < len(arr):
        if integer != arr[ind]:
            integer += 1
            count += 1
        else:
            ind += 1
            integer += 1
    integer += k - count - 1
    return integer

arr = [1]
k = 1
print(findKthPositive(arr, k))
