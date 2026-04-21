class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = 0
        n = len(nums)

        if(n == 1):
            return nums[0]

        # start from 0
        f = [0] * n
        f[0] = nums[0]

        profit = nums[0]
        maxSeen = 0
        for i in range(2, n - 1):
            maxSeen = max(maxSeen, f[i - 2])
            f[i] = maxSeen + nums[i]
            profit = max(profit, f[i])

        # start from 1
        maxSeen = 0
        profit = max(profit, nums[1])
        f = [0] * n
        f[1] = nums[1]
        for i in range(2, n):
            maxSeen = max(maxSeen, f[i - 2])
            f[i] = maxSeen + nums[i]
            profit = max(profit, f[i])

        return profit

