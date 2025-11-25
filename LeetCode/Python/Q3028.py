class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        loc = 0

        for num in nums:
            loc += num

            if(loc == 0):
                ans += 1

        return ans