class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        f = [[0, 0] for i in range(n)]
        
        ans = 0
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if(nums[i] < nums[j]):
                    f[i][0] = max(f[i][0], f[j][1] + 1)
                if(nums[i] > nums[j]):
                    f[i][1] = max(f[i][1], f[j][0] + 1)

            ans = max(ans, f[i][0], f[i][1])

        return ans + 1