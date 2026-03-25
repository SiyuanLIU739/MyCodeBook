class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = []
        for i in range(m):
            visited.append([False] * n)

        ans = 0
        for i in range(m):
            for j in range(n):
                if(not visited[i][j] and grid[i][j] == 1):
                    ans = max(ans, self.dfs(grid, i, j, m, n, visited))

        return ans
    
    def dfs(self, grid, i, j, m, n, visited):
        visited[i][j] = True
        area = 1

        if(i != 0 and not visited[i - 1][j] and grid[i - 1][j]):
            area += self.dfs(grid, i - 1, j, m, n, visited)

        if(j != 0 and not visited[i][j - 1] and grid[i][j - 1]):
            area += self.dfs(grid, i, j - 1, m, n, visited)

        if(i != m - 1 and not visited[i + 1][j] and grid[i + 1][j]):
            area += self.dfs(grid, i + 1, j, m, n, visited)
        
        if(j != n - 1 and not visited[i][j + 1] and grid[i][j + 1]):
            area += self.dfs(grid, i, j + 1, m, n, visited)

        return area