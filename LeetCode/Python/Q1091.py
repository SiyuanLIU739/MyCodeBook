class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0] == 1):
            return -1
        
        n = len(grid)
        visited = [[10000 + 7] * n for i in range(n)]
        visited[0][0] = 1
        queue = [(0, 0)]

        steps = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while(len(queue) != 0):
            x, y = queue.pop(0)

            for step in steps:
                nextx = x + step[0]
                nexty = y + step[1]

                if(nextx < 0 or nextx == n or nexty < 0 or nexty == n):
                    continue
                if(grid[nextx][nexty] == 0 and visited[nextx][nexty] > visited[x][y] + 1):
                    visited[nextx][nexty] = visited[x][y] + 1
                    queue.append((nextx, nexty))
                
                    if(nextx == n - 1 and nexty == n - 1):
                        return visited[nextx][nexty]
        
        if(visited[n - 1][n - 1] > n * n):
            return -1
        return visited[n - 1][n - 1]