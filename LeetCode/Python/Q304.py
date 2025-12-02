class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        # cal the sum
        sum_matrix = [[0] * (n + 1)]
        for i in range(m):
            sum_matrix.append([0])
            for j in range(n):
                sum_matrix[-1].append(sum_matrix[-2][j + 1] + sum_matrix[-1][-1] + matrix[i][j] - sum_matrix[i][j])

        self.sum_matrix = sum_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1

        return self.sum_matrix[row2][col2] + self.sum_matrix[row1][col1] - self.sum_matrix[row2][col1] - self.sum_matrix[row1][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)