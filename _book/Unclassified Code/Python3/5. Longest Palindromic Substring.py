def longestPalindrome(s: str) -> str:
    n = len(s)
    ans = ""

    dp = [[False] * n for _ in range(n)]

    for l in range(n):
        for i in range(n):
            j = i + l
            if j >= n:
                break
            elif j == i:
                dp[i][j] = True
            elif j == i+1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
            if dp[i][j] and l >= len(ans):
                ans = s[i:j+1]
    return ans

s = "aaaa"

print(longestPalindrome(s))