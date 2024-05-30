class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = 0

        nums = [num for num in nums if num > 0]
        
        for num in nums:
            if(num > max_num):
                max_num = num

        nums = set(nums)

        if(len(nums) == max_num):
            return max_num + 1
        
        ans = 1

        while(ans in nums):
            ans += 1

        return ans