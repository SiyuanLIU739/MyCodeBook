class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = 0

        ans = 1000000
        left = 0
        range_sum = 0
        for i in range(len(nums)):
            range_sum += nums[i]

            while(range_sum >= target):
                ans = min(ans, i - left + 1)
                range_sum -= nums[left]
                left += 1

            

        if(ans == 1000000):
            return 0

        return ans