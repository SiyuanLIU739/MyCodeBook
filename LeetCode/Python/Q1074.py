class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        f = [[matrix[0][0]]]
        for i in range(1, n):
            f[0].append(f[0][-1] + matrix[0][i])

        for i in range(1, m):
            f.append([f[-1][0] + matrix[i][0]])
            for j in range(1, n):
                f[-1].append(f[-2][j] + f[-1][-1] - f[-2][j - 1] + matrix[i][j])
        ans = 0
        for i in range(m):
            for j in range(i, m):
                prevMap = {0: 1}
                for k in range(n):
                    sum = self.calMatrix(i, j, k, f)
                    if((sum - target) in prevMap.keys()):
                        ans += prevMap[sum - target]
                    if(sum not in prevMap.keys()):
                        prevMap[sum] = 0
                    prevMap[sum] += 1
        return ans
    
    def calMatrix(self, i, j, k, f):
        if(i == 0):
            return f[j][k]
        return f[j][k] - f[i - 1][k]