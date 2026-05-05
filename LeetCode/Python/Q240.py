class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = n - 1

        while(x < m and y >= 0):
            current = matrix[x][y]
            if(target == current):
                return True
            if(target < current):
                y -= 1
            else:
                x += 1
        
        return False