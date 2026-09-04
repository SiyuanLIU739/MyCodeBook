class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [n] * n
        f[0] = 0

        for i in range(n):
            for j in range(nums[i] + 1):
                if(i + j >= n):
                    break
                f[i + j] = min(f[i + j], f[i] + 1)

        return f[n - 1]