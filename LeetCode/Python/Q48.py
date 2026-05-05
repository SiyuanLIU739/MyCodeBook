class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        corner = [0, 0]

        while(n > 1):
            for y in range(n - 1):
                x = 0
                this = [x, y]
                next = [y, n - x - 1]
                takeout = matrix[corner[0] + this[0]][corner[1] + this[1]]
                for i in range(4):
                    value = matrix[corner[0] + next[0]][corner[1] + next[1]]
                    matrix[corner[0] + next[0]][corner[1] + next[1]] = takeout
                    takeout = value
                    this[0] = next[0]
                    this[1] = next[1]
                    next[0] = this[1]
                    next[1] = n - this[0] - 1
                     
            corner[0] += 1
            corner[1] += 1
            n -= 2

        