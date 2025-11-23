class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        inf = 400000000
        ans = 0
        f = [[0, -inf, -inf]]

        nums.insert(0, 0)

        mod = 10002
        for i in range(1, len(nums)):
            f.append([-1] * 3)
            for j in range(3):
                f[i][j] = max(f[i - 1][j], f[i - 1][(j + mod - nums[i]) % 3] + nums[i])

            ans = max(ans, f[i][0])

        return ans