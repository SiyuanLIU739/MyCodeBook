class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        line = [0] * 9
        col = [0] * 9
        sqr = [[0] * 3 for i in range(3)]

        for i in range(9):
            for j in range(9):
                try:
                    board[i][j] = int(board[i][j])
                    line[i] = line[i] | (1 << board[i][j])
                    col[j] = col[j] | (1 << board[i][j])
                    sqr[i // 3][j // 3] = sqr[i // 3][j // 3] | (1 << board[i][j])
                except:
                    board[i][j] = -1
                

        self.board = board

        self.search(0, 0, line, col, sqr)

        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])

    def search(self, x, y, line, col, sqr):
        nextx = x
        nexty = y
        if(y != 8):
            nexty = y + 1
        else:
            nextx += 1
            nexty = 0

        if(self.board[x][y] > 0):
            if(x == 8 and y == 8):
                return True

            return self.search(nextx, nexty, line, col, sqr)
        

        for num in range(1, 10):
            if((line[x] & (1 << num)) == 0 and (col[y] & (1 << num)) == 0 and (sqr[x // 3][y // 3] & (1 << num)) == 0):
                line[x] = line[x] | (1 << num)
                col[y] = col[y] | (1 << num)
                sqr[x // 3][y // 3] = sqr[x // 3][y // 3] | (1 << num)
                self.board[x][y] = num

                if(x == 8 and y == 8):
                    return True
                
                result = self.search(nextx, nexty, line, col, sqr)

                if(result):
                    return True
                
                line[x] = line[x] & ~(1 << num)
                col[y] = col[y] & ~(1 << num)
                sqr[x // 3][y // 3] = sqr[x // 3][y // 3] & ~(1 << num)
                self.board[x][y] = -1