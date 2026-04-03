class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [[False] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if(word[0] != board[i][j]):
                    continue
                if(self.dfs(board, i, j, word, 0, visited)):
                    return True
                
        return False
    
    def dfs(self, board, x, y, word, pos, visited):
        visited[x][y] = True

        if(pos == len(word) - 1):
            return True
        
        m = len(board)
        n = len(board[0])

        # up
        if(x != 0 and board[x - 1][y] == word[pos + 1] and not visited[x - 1][y]):
            if(self.dfs(board, x - 1, y, word, pos + 1, visited)):
                return True
        
        # down
        if(x + 1 != m and board[x + 1][y] == word[pos + 1] and not visited[x + 1][y]):
            if(self.dfs(board, x + 1, y, word, pos + 1, visited)):
                return True
            
        # right
        if(y + 1 != n and board[x][y + 1] == word[pos + 1] and not visited[x][y + 1]):
            if(self.dfs(board, x, y + 1, word, pos + 1, visited)):
                return True
            
        # left
        if(y != 0 and board[x][y - 1] == word[pos + 1] and not visited[x][y - 1]):
            if(self.dfs(board, x, y - 1, word, pos + 1, visited)):
                return True
            
        visited[x][y] = False
        return False