class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum = nums[0] + nums[1]
        ans = -1

        for i in range(2, len(nums)):
            if(sum > nums[i]):
                ans = max(ans, sum + nums[i])
            sum += nums[i]

        return ans