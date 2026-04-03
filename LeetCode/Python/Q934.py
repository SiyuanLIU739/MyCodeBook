class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[10000 + 7] * n for i in range(n)]

        ans = n * n * 2
        queue = []

        for i in range(n):
            for j in range(n):
                if(grid[i][j] == 1):
                    visited[i][j] = 0
                    queue.append((i, j))
                    break
            if(len(queue) > 0):
                break

        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while(len(queue) != 0):
            x, y = queue.pop(0)

            for step in steps:
                nextx = x + step[0]
                nexty = y + step[1]

                if(nextx < 0 or nextx == n or nexty < 0 or nexty == n):
                    continue

                if(grid[nextx][nexty] == 1 and visited[nextx][nexty] > visited[x][y]):
                    visited[nextx][nexty] = visited[x][y]
                    queue.append((nextx, nexty))

                elif(grid[nextx][nexty] == 0 and visited[nextx][nexty] > visited[x][y] + 1):
                    visited[nextx][nexty] = visited[x][y] + 1
                    queue.append((nextx, nexty))

        for i in range(n):
            for j in range(n):
                if(grid[i][j] == 1 and visited[i][j] != 0):
                    ans = min(ans, visited[i][j])

        return ans
