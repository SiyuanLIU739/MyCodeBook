from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for i in range(m)]

        q = deque()

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == '0' or visited[i][j]):
                    continue
                ans += 1

                visited[i][j] = True
                q.append((i, j))

                while(q):
                    x, y = q.popleft()

                    for move in moves:
                        next_x = x + move[0]
                        next_y = y + move[1]

                        if(next_x < 0 or next_x >= m or next_y < 0 or next_y >= n):
                            continue

                        if(grid[next_x][next_y] == '0' or visited[next_x][next_y]):
                            continue

                        visited[next_x][next_y] = True

                        q.append((next_x, next_y))

        return ans