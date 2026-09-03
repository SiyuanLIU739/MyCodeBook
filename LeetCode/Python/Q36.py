class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            line = set()
            for j in range(9):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] in line):
                    return False
                line.add(board[i][j])

        for i in range(9):
            col = set()
            for j in range(9):
                if(board[j][i] == "."):
                    continue

                if(board[j][i] in col):
                    return False

                col.add(board[j][i])

        for s in range(0, 7, 3):
            for t in range(0, 7, 3):
                square = set()
                for i in range(3):
                    for j in range(3):
                        if(board[s + i][t + j] == '.'):
                            continue
                        if(board[s + i][t + j] in square):
                            return False

                        square.add(board[s + i][t + j])

        return True
                    
