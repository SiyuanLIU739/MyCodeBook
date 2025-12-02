class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while(i + 2 < len(nums)):
            while(i + 2 < len(nums) and nums[i] == nums[i + 2]):
                nums.pop(i)
            i += 1

        return len(nums)