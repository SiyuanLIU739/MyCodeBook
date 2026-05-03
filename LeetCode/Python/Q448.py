class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)

        ans = []
        for i in range(n):
            if(i + 1 not in nums):
                ans.append(i + 1)

        return ans
    

# upd
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if(nums[abs(nums[i]) - 1] > 0):
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        ans = []
        for i in range(len(nums)):
            if(nums[i] > 0):
                ans.append(i + 1)
        
        return ans