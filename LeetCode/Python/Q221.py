class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        f = [[0] * n for i in range(m)]

        max_edge = 0
        for i in range(m):
            for j in range(n):

                if(matrix[i][j] == '1'):
                    if(i != 0 and j != 0):
                        f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1])

                    f[i][j] += 1
                    max_edge = max(max_edge, f[i][j])
                
        return max_edge ** 2
    
# if the spot is at edge, the max square edge ending at this spot should be 1
# otherwise, it should be the smallest around + 1