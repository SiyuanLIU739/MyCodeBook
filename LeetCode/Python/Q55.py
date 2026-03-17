class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        if(n == 0):
            return True
            
        maxReach = 0
        for i in range(n):
            if(i > maxReach):
                break
            
            maxReach = max(i + nums[i], maxReach)

            if(maxReach >= n):
                return True
            
        return False