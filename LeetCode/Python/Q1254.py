class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for i in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    continue

                if(visited[i][j]):
                    continue

                if(self.dfs(grid, visited, i, j)):
                    ans += 1

        return ans

    def dfs(self, grid, visited, i, j):
        visited[i][j] = True
        m = len(grid)
        n = len(grid[0])

        ret = True
        if(i == 0 or i == m - 1 or j == 0 or j == n - 1):
            ret = False

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for d in directions:
            next_i = i + d[0]
            next_j = j + d[1]

            if(next_i < 0 or next_i >= m or next_j < 0 or next_j >= n):
                continue

            if(grid[next_i][next_j] == 1):
                continue

            if(visited[next_i][next_j]):
                continue


            ret = self.dfs(grid, visited, next_i, next_j) and ret

        return ret
# [0,0,1,1,0,1,0,0,1,0]
# [1,1,0,1,1,0,1,1,1,0]
# [1,0,1,1,1,0,0,1,1,0]
# [0,1,1,0,0,0,0,1,0,1]
# [0,0,0,0,0,0,1,1,1,0]
# [0,1,0,1,0,1,0,1,1,1]
# [1,0,1,0,1,1,0,0,0,1]
# [1,1,1,1,1,1,0,0,0,0]
# [1,1,1,0,0,1,0,1,0,1]
# [1,1,1,0,1,1,0,1,1,0]