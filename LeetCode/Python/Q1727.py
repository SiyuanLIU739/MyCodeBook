class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        f = [0] * m
        h = [0] * n

        for i in range(m):
            for j in range(n):
                f[i] += matrix[i][j]
                h[j] += matrix[i][j]

        