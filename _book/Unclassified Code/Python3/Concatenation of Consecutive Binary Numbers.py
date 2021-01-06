def concatenatedBinary(n: int) -> int:
    a = 0
    b = 0
    power = 1
    for i in range(1, n + 1):
        b = a * (2 ** power) + i
        if i == 2 ** power - 1:
            power += 1
        a = b
    return b % (10 ** 9 + 7)

print(concatenatedBinary(99999))
