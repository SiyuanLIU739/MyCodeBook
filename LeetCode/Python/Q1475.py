class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            price = prices[i]

            discount = 0
            for j in range(i + 1, len(prices)):
                if(prices[j] <= price):
                    discount = prices[j]
                    break
            
            price = price - discount
            ans.append(price)

        return ans