class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        visited = [[False] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if(board[i][j] == 'X' or visited[i][j]):
                    continue
                self.minX = i
                self.maxX = i
                self.minY = j
                self.maxY = j
                self.dfs(board, i, j, visited)
                if(self.minX != 0 and self.minY != 0 and self.maxX != m - 1 and self.maxY != n - 1):
                    self.dfs_change(board, i, j)

    def dfs(self, board, x, y, visited):
        m = len(board)
        n = len(board[0])

        visited[x][y] = True
        self.minX = min(x, self.minX)
        self.minY = min(y, self.minY)
        self.maxX = max(x, self.maxX)
        self.maxY = max(y, self.maxY)

        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for step in steps:
            nextx = x + step[0]
            nexty = y + step[1]

            if(nextx < 0 or nexty < 0 or nextx == m or nexty == n):
                continue

            if(board[nextx][nexty] != 'X' and not visited[nextx][nexty]):
                self.dfs(board, nextx, nexty, visited)

    def dfs_change(self, board, x, y):
        m = len(board)
        n = len(board[0])

        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        board[x][y] = 'X'
        for step in steps:
            nextx = x + step[0]
            nexty = y + step[1]

            if(nextx < 0 or nexty < 0 or nextx == m or nexty == n):
                continue

            if(board[nextx][nexty] != 'X'):
                self.dfs_change(board, nextx, nexty)