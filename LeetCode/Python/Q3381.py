class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        f = []
        presum = [0]
        ans = -1000000000 * 2 * 100000 - 100

        for i in range(k):
            f.append(0)

        for i in range(1, len(nums)):
            # cal presum
            presum.append(presum[-1] + nums[i])
            if(i < k):
                continue

            if(f[i - k] > 0):
                f.append(f[i - k] + presum[i] - presum[i - k])
            else:
                f.append(presum[i] - presum[i - k])

            ans = max(ans, f[-1])

        return ans