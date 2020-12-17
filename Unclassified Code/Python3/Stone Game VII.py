def stoneGameVII(stones: [int]) -> int:
    alice = True
    left = 0
    right = len(stones) - 1
    res = 0
    while left+1 < right:
        if alice:
            if min(stones[left], stones[right-1]) > min(stones[left+1], stones[right]):
                right -= 1
            else:
                left += 1
            alice = not alice
        else:
            if max(stones[left], stones[right - 1]) >= max(stones[left + 1], stones[right]):
                add = stones[left]
                left += 1
            else:
                add = stones[right]
                right -= 1
            alice = not alice
            res += add
    if len(stones) % 2 == 0:
        res += stones[left]
    else:
        res += min(stones[left], stones[right])
    return res

stones = [7,90,5,1,100,10,10,2]
print(stoneGameVII(stones))