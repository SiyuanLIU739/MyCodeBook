class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ak = (101 // k) * k
        mod = 1000000000 + 7

        # prepare grid
        grid = [[0] * (n + 1)] + grid
        for i in range(1, m + 1):
            grid[i] = [0] + grid[i]

        # prepare f
        f = []
        for i in range(m + 1):
            f.append([])
            for j in range(n + 1):
                f[-1].append([0] * k)
        f[0][1][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for l in range(0, k):
                    a = (l - grid[i][j] + ak) % k
                    f[i][j][l] = (f[i - 1][j][a] + f[i][j - 1][a]) % mod

        return f[m][n][0]