class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        current_sum = 0
        left = 0

        ans = 1
        for right in range(len(nums)):
            current_sum += nums[right]

            while((right - left + 1) * nums[right] - current_sum > k):
                current_sum -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans