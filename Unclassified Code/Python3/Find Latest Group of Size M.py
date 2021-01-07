class Solution:
    def __init__(self, n):
        self.ans = n
    def findLatestStep(self, arr: [int], m: int) -> int:
        n = len(arr)
        self.ans = 0

        def checkOnes(i, j, zero_ind):
            if j - i + 1 < m:
                return
            if j - i + 1 == m:
                self.ans = max(zero_ind, self.ans)
            else:
                temp = 1
                while not (i <= arr[zero_ind-temp] <= j+1):
                    temp += 1
                if i <= arr[zero_ind-temp] <= j+1 and zero_ind-temp >= 0:
                    checkOnes(i, arr[zero_ind - temp] - 2, zero_ind - temp)
                    checkOnes(arr[zero_ind - temp], j, zero_ind - temp)

        checkOnes(0, n - 1, n)
        return self.ans

arr = [1,9,12,6,4,5,3,13,2,11,10,7,8]
m = 4
S = Solution(len(arr))
print(S.findLatestStep(arr,m))