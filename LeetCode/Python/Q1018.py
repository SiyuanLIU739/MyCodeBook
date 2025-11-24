class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        value = 0

        for num in nums:
            value = value * 2 + num
            ans.append(value % 5 == 0)

        return ans