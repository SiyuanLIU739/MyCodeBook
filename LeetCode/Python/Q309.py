class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = -2000 * 5000

        n = len(prices)
        prices = [0] + prices
        fHave = [minValue] * (n + 1)
        fSell = [0] * (n + 1)

        maxSell = 0
        maxHave = minValue
        profit = 0
        for i in range(1, n + 1):
            if(i > 2):
                maxSell = max(maxSell, fSell[i - 2])
            if(i > 1):
                maxHave = max(maxHave, fHave[i - 1])

            fHave[i] = max(fHave[i - 1], maxSell - prices[i])
            fSell[i] = maxHave + prices[i]

            profit = max(profit, fSell[i])

        return profit