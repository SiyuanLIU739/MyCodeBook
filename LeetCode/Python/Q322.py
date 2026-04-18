class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxAmount = 9999

        f = [maxAmount] * amount
        f[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if(i >= coin):
                    f[i] = min(f[i], f[i - coin] + 1)

        if(f[amount] >= maxAmount):
            return -1
        
        return f[amount]