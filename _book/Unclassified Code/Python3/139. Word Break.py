def wordBreak(s: str, wordDict: [str]) -> bool:
    n = len(s)
    if n == 0:
        return False
    i = 0
    while i < n - 1:
        if s[:i + 1] in wordDict:
            s = s[i + 1:]
            n -= i+1
            i = 0
        else:
            i += 1
    if s[:i+1] in wordDict:
        return True
    else:
        return False

s = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(s,wordDict))