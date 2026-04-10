class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            dp[i] = sum(dp[i - num] for num in nums if i >= num)
        return dp[target]