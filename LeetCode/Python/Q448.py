class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)

        ans = []
        for i in range(n):
            if(i + 1 not in nums):
                ans.append(i + 1)

        return ans