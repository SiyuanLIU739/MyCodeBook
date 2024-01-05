class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inf = 25000
        nums.insert(0, -100000)
        n = len(nums)
        f = [0]

        for i in range(1, n):
            f.append(0)
            for j in range(i):
                if(nums[j] < nums[i]):
                    f[i] = max(f[i], f[j] + 1)

        return f[n - 1]