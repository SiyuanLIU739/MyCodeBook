class Solution:
    def integerBreak(self, n: int) -> int:
        f = [[0] * (n + 1) for i in range(n + 1)]

        f[0][0] = 1
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                for m in range(j - 1, i):
                    f[i][j] = max(f[i][j], f[m][j - 1] * (i - m))
                if(i == n and j >= 2):
                    ans = max(ans, f[i][j])

        return ans