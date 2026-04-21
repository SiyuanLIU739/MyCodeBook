class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        f = [0] * n

        ans = -100001
        for i in range(n):
            f[i] = nums[i]
            if(i > 0 and f[i - 1] > 0):
                f[i] += f[i - 1]
            ans = max(ans, f[i])

        return ans