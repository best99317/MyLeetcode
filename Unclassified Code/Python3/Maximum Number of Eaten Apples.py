def eatenApples(apples: [int], days: [int]) -> int:
    bag = []
    day = 0
    n = len(apples)
    for i in range(n):
        if not bag:
            if apples[i] != 0:
                apples[i] -= 1
                day += 1
                if apples[i] > 0 and days[i] > 1:
                    bag.append([i+days[i]-1, apples[i]])
                print(bag)
        else:
            if apples[i] != 0:
                bag.append([i+days[i]-1, apples[i]])
                bag.sort(reverse=True)
                bag[-1][1] -= 1
                day += 1
            else:
                bag[-1][1] -= 1
                day += 1
            if bag[-1][1] == 0:
                bag.pop()
            while bag and bag[-1][0] <= i:
                bag.pop()
            print(bag)
    i = 0
    while bag:
        bag[-1][1] -= 1
        day += 1
        i += 1
        if bag[-1][1] == 0:
            bag.pop()
        while bag and bag[-1][0] <= n+i-1:
            bag.pop()
    return day

print(eatenApples([1], [2]))