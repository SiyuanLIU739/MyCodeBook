class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        MAXX = 1024
        
        dp = [[[False]*MAXX for _ in range(n)] for _ in range(m)]
        
        dp[0][0][grid[0][0]] = True
        
        for i in range(m):
            for j in range(n):
                for x in range(MAXX):
                    if not dp[i][j][x]:
                        continue
        
                    if i+1 < m:
                        dp[i+1][j][x ^ grid[i+1][j]] = True
                    if j+1 < n:
                        dp[i][j+1][x ^ grid[i][j+1]] = True

        for i in range(MAXX):
            if(dp[m - 1][n - 1][i]):
                return i
            
sol = Solution()
grid = [[2,7,5]]
print(sol.minCost(grid))