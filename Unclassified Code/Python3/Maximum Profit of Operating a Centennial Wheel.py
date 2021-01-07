def minOperationsMaxProfit(customers: [int], boardingCost: int, runningCost: int) -> int:
    cur_cus = 0
    cur_prof = 0
    max_prof = -float("inf")
    best_rot = -1
    n = len(customers)
    i = 0
    num_rot = 0
    while cur_cus > 0 or i < n:
        if i < n:
            cur_prof += min(cur_cus + customers[i], 4) * boardingCost - runningCost
            cur_cus = max(0, cur_cus + customers[i] - 4)
            i += 1
        else:
            cur_prof += min(cur_cus, 4) * boardingCost - runningCost
            cur_cus = max(0, cur_cus - 4)
        num_rot += 1
        if cur_prof > max_prof:
                max_prof = cur_prof
                best_rot = num_rot
    return best_rot if max_prof > 0 else -1

customers = [8,3]
boardingCost = 5
runningCost = 6

print(minOperationsMaxProfit(customers, boardingCost, runningCost))