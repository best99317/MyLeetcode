def maximumUnits(boxTypes: [[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=(lambda x:x[1]), reverse=True)
        print(boxTypes)
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if truckSize >= boxTypes[i][0]:
                res += boxTypes[i][1] * boxTypes[i][0]
                truckSize -= boxTypes[i][0]
                i += 1
            else:
                print(truckSize)
                res += truckSize * boxTypes[i][1]
                break
        return res

print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))