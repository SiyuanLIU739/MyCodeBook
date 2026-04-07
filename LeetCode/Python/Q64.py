class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        f = [[200 * 200 * 200] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    f[i][j] = grid[i][j]
                    continue

                if(i == 0):
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif(j == 0):
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]

        return f[m - 1][n - 1]
