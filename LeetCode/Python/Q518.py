class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        f = [0] * (amount + 1)

        f[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] += f[i - coin]

        return f[amount]