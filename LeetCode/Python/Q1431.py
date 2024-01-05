class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = 0

        for candy in candies:
            if(candy > maxC):
                maxC = candy

        ans = []
        for candy in candies:
            ans.append((candy + extraCandies) >= maxC)

        return ans