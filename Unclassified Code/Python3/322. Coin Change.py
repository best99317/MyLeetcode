def coinChange(coins: [int], amount: int) -> int:
    if amount == 0:
        return 0
    coins.sort(reverse=True)
    for i in coins:
        if amount >= i:
            amount -= i
            return coinChange(coins, amount) + 1


coins = [1, 2, 5]
amount = 11

print(coinChange(coins, amount))
