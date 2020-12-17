def multiply(num1: str, num2: str) -> str:
    m = len(num1)
    n = len(num2)
    res = ""

    def addStrings(num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

    for i in range(m - 1, -1, -1):
        temp_res = ""
        tens = 0
        for j in range(n - 1, -1, -1):
            ans = int(num1[i]) * int(num2[j])
            ones = (ans + tens) % 10
            tens = (ans + tens) // 10
            temp_res = str(ones) + temp_res
            if j == 0 and tens > 0:
                temp_res = str(tens) + temp_res
        temp_res = temp_res + '0' * (m-1-i)
        res = addStrings(res, temp_res)
    return res

num1 = "123"
num2 = "456"

print(multiply(num1,num2))
