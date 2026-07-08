from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        orange_left = 0

        inf = 100
        rotten = [[inf] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    rotten[i][j] = 0
                    q.append((i, j))
                elif(grid[i][j] == 1):
                    orange_left += 1
        
        ans = 0
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while(q):
            x, y = q.popleft()
            minute = rotten[x][y]

            for move in moves:
                next_x = x + move[0]
                next_y = y + move[1]

                if(next_x < 0 or next_x >= m or next_y < 0 or next_y >= n):
                    continue
                if(grid[next_x][next_y] != 1 or rotten[next_x][next_y] <= minute + 1):
                    continue

                rotten[next_x][next_y] = minute + 1
                q.append((next_x, next_y))
                orange_left -= 1

            ans = max(ans, minute)
            
        if(orange_left != 0):
            return -1
        return ans