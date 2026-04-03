class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        lastLine = [0] * n

        ans = 0
        for i in range(m):
            line = []
            preSum = 0
            for j in range(n):
                line.append(lastLine[j] + grid[i][j] + preSum)
                preSum += grid[i][j]
                if(line[-1] <= k):
                    ans += 1
            lastLine = line

        return ans