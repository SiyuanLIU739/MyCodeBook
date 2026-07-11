class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if(num not in count.keys()):
                count[num] = 0
            count[num] += 1

        ans = 0
        for num in nums:
            if(num + 1 in count.keys()):
                ans = max(ans, count[num + 1] + count[num])
            if(num - 1 in count.keys()):
                ans = max(ans, count[num - 1] + count[num])

        return ans