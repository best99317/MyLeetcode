def reorderSpaces(text: str) -> str:
    count_space = 0
    count_word = 0
    n = len(text)
    res = ""
    for i in range(n):
        if text[i] == " ":
            count_space += 1
        if i + 1 < n and text[i] != " " and text[i + 1] == " ":
            count_word += 1
        if i == n - 1 and text[i] != " ":
            count_word += 1
    if count_word == 1:
        interval = ""
        intervals = 0
        tail = " " * count_space
    else:
        intervals = count_word - 1
        interval = " " * (count_space // intervals)
        tail = " " * (count_space % intervals)
    new_space = False
    counter = 0
    for i in range(n):
        if text[i] != " ":
            res += text[i]
            if i + 1 < n and text[i + 1] == " ":
                new_space = True
        if new_space and counter < intervals:
            res += interval
            counter += 1
            new_space = False
    res += tail
    return res

text = "  walks  udp package   into  bar a"
print(reorderSpaces(text))