def maximumBinaryString(binary: str) -> str:
    n = len(binary)
    while '00' in binary or '10' in binary:
        temp = binary
        for i in range(n-1):
            if binary[i:i+2] == '00' and '0':
                binary = binary[:i] + '1' + binary[i+1:]
        # print(binary)
        while '10' in binary:
            from collections import Counter
            count = Counter(list(binary))
            if '00' in binary or count['0'] < 2:
                break
            for i in range(n-1):
                if binary[i:i+2] == '10' and '0' in binary[:i]:
                    binary = binary[:i] + '01' + binary[i+2:]
            
        # print(binary)
        # from collections import Counter
        # count = Counter(list(binary))
        # if count['0'] < 2:
        #     break
        if binary == temp:
            break
    return binary

print(maximumBinaryString("000110"))