class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        return len(setnums) != len(nums)