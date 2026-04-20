class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        maxSell = k

        f = [[0, -1000 * 2000] for i in range(maxSell + 1)]

        profit = 0
        for p in prices:
            for j in range(maxSell, 0, -1):
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
                profit = max(profit, f[j][0])

        return profit