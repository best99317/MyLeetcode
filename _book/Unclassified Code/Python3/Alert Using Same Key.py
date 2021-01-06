def alertNames(keyName: [str], keyTime: [str]) -> [str]:
    dic = dict()
    names = set()
    n = len(keyName)
    temp = zip(keyTime, keyName)
    temp = sorted(temp)
    keyTime, keyName = zip(*temp)

    def checkHour(time1, time2):
        hour1 = int(time1.split(":")[0])
        minute1 = int(time1.split(":")[1])
        hour2 = int(time2.split(":")[0])
        minute2 = int(time2.split(":")[1])
        return (hour2 - hour1) * 60 + (minute2 - minute1) <= 60

    for i in range(n):
        if keyName[i] not in dic:
            dic[keyName[i]] = [keyTime[i] + "1"]
        elif keyName[i] not in names:
            for j, time in enumerate(dic[keyName[i]]):
                if checkHour(time[:5], keyTime[i]):
                    dic[keyName[i]][j] = dic[keyName[i]][j][:5] + str(int(dic[keyName[i]][j][5]) + 1)
                    dic[keyName[i]].append(keyTime[i] + "1")
                    if time[-1] == "3":
                        names.add(keyName[i])
                else:
                    dic[keyName[i]].remove(time)
                    dic[keyName[i]].append(keyTime[i] + "1")
    res = list(names)
    res.sort()
    return res

# keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
# keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# keyName = ["alice","alice","alice","bob","bob","bob","bob"]
# # keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
print(alertNames(keyName, keyTime))