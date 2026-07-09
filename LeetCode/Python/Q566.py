class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if(m * n != r * c):
            return mat
        
        i = 0
        j = 0
        k = 0
        w = 0
        ans = [[0] * c for _ in range(r)]
        while(not i == m):
            ans[k][w] = mat[i][j]

            j += 1
            if(j == n):
                j = 0
                i += 1

            w += 1
            if(w == c):
                w = 0
                k += 1

        return ans