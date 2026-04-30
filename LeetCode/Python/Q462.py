class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        target = 0
        if(n % 2 == 1):
            target = nums[n // 2]
        else:
            target = (nums[n // 2] + nums[n // 2 - 1]) // 2

        ans = 0
        for num in nums:
            ans += abs(num - target)
        
        return ans