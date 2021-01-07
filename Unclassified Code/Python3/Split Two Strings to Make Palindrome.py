def checkPalindromeFormation(a: str, b: str) -> bool:
    n = len(a)

    def checkP(temp):
        if len(temp) % 2:
            if temp[:len(temp) // 2] == temp[len(temp) // 2 + 1:][::-1]:
                return True
            else:
                return False
        else:
            if temp[:len(temp) // 2] == temp[len(temp) // 2:][::-1]:
                return True
            else:
                return False

    for i in range(n // 2 + 1):
        if a[i] != b[-i - 1] and b[i] != a[-i - 1]:
            if checkP(a[:i] + b[i:]) or checkP(b[:i] + a[i:]) or checkP(a[:-i]+b[-i:]) or checkP(b[:-i]+a[-i:]):
                return True
            else:
                return False
        if n % 2 == 0 and i == n // 2 - 1:
            return True
    return False

# a[:7] + b[7:]
# a[:-7]+b[-7:]
a = "abcde"
b = "ighba"
print(checkPalindromeFormation(a,b))