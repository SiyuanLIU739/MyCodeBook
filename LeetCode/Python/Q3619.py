class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for i in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    continue

                if(visited[i][j]):
                    continue

                sum_island = self.dfs(grid, visited, i, j)

                if(sum_island % k == 0):
                    ans += 1


        return ans

    def dfs(self, grid, visited, i, j):
        visited[i][j] = True
        s = grid[i][j]
        m = len(grid)
        n = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in directions:
            next_i = i + d[0]
            next_j = j + d[1]

            if(next_i < 0 or next_i >= m or next_j < 0 or next_j >= n):
                continue

            if(grid[next_i][next_j] == 0):
                continue

            if(visited[next_i][next_j]):
                continue

            s += self.dfs(grid, visited, next_i, next_j)

        return s