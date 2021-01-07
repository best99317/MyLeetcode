def breakfastNumber(staple: [int], drinks: [int], x: int) -> int:
    staple.sort()
    drinks.sort()

    def findless(num, target):
        if target >= num[-1]:
            return len(num)
        if target < num[0]:
            return 0
        left = 0
        right = len(num) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if num[middle] < target:
                left = middle + 1
            elif num[middle] > target:
                right = right - 1
            else:
                return middle + 1
        return middle

    res = 0
    for i in staple:
        res += findless(drinks, x - i)
    return res % (1000000007)

def breakfastNumber1(staple: [int], drinks: [int], x: int) -> int:
    res = 0
    for i in staple:
        for j in drinks:
            if i + j <=x:
                res += 1
    return res % (1000000007)
# staple = [10,20,5]
# drinks = [5,5,2]
# x = 15
staple = [0,5,1,1,7,10,10,102,99,61,97]
drinks = [6,98,23,10,59,60,102,99]
x = 100
print(breakfastNumber(staple, drinks, x), " | ", breakfastNumber1(staple, drinks, x))













class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        



















