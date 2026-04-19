class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        lowestPrice = 100001

        for p in prices:
            maxP = max(maxP, p - lowestPrice)
            lowestPrice = min(lowestPrice, p)

        return maxP