class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maxpd = []
        minpd = []
        for i in range(m):
            maxpd.append([0] * n)
            minpd.append([0] * n)

        maxpd[0][0] = grid[0][0]
        minpd[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    continue
                # only come from left
                if(i == 0):
                    if(grid[i][j] >= 0):
                        maxpd[i][j] = maxpd[i][j - 1] * grid[i][j]
                        minpd[i][j] = minpd[i][j - 1] * grid[i][j]
                    else:
                        maxpd[i][j] = minpd[i][j - 1] * grid[i][j]
                        minpd[i][j] = maxpd[i][j - 1] * grid[i][j]
                # only come from up
                elif(j == 0):
                    if(grid[i][j] >= 0):
                        maxpd[i][j] = maxpd[i - 1][j] * grid[i][j]
                        minpd[i][j] = minpd[i - 1][j] * grid[i][j]
                    else:
                        maxpd[i][j] = minpd[i - 1][j] * grid[i][j]
                        minpd[i][j] = maxpd[i - 1][j] * grid[i][j]
                # come from both
                else:
                    if(grid[i][j] >= 0):
                        maxpd[i][j] = max(maxpd[i][j - 1], maxpd[i - 1][j]) * grid[i][j]
                        minpd[i][j] = min(minpd[i][j - 1], minpd[i - 1][j]) * grid[i][j]
                    else:
                        maxpd[i][j] = min(minpd[i][j - 1], minpd[i - 1][j]) * grid[i][j]
                        minpd[i][j] = max(maxpd[i][j - 1], maxpd[i - 1][j]) * grid[i][j]
        
        if(maxpd[m - 1][n - 1] < 0):
            return -1
        return maxpd[m - 1][n - 1] % (1000000000 + 7)