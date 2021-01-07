def numMatchingSubseq(S: str, words: [str]) -> int:
    def subSequence(S: str, word: str):
        m = len(S)
        n = len(word)
        p1 = 0
        p2 = 0
        if m == 0:
            return False
        if n == 0:
            return True
        while p1 < m and p2 < n:
            if S[p1] == word[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        if p2 < n:
            return False
        if p1 <= m:
            return True

    res = 0
    for w in words:
        if subSequence(S,w):
            res += 1
    return res

S = "abcde"
words = ["a", "bb", "acd", "ace"]

print(numMatchingSubseq(S, words))
