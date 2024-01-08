class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        f = {}
        n = len(nums)

        for i in range(1, n):
            for j in range(i):
                k = nums[i] - nums[j]
                l = 0
                if (j, k) in f.keys():
                    l = f[(j, k)]
                if (i, k) not in f.keys():
                    f[(i, k)] = 0
                f[(i, k)] += l
                f[(i, k)] += 1

        ans = 0
        for an, d in f.keys():
            ans += f[(an, d)]

        ans -= (n * (n - 1) / 2)
        return ans