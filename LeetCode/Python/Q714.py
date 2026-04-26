class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f = [[- 5 * 10000 * 5 * 10000, - 5 * 10000 * 5 * 10000] for i in range(len(prices))]
        f[0][0] = 0
        f[0][1] = -prices[0] - fee

        ans = 0
        j0seen = 0
        j1seen = -prices[0] - fee
        for i in range(1, len(prices)):
            f[i][1] = j0seen - prices[i] - fee
            f[i][0] = j1seen + prices[i]

            ans = max(ans, f[i][0])

            j0seen = max(f[i][0], j0seen)
            j1seen = max(f[i][1], j1seen)
            
        return ans