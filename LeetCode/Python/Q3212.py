class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        lastLineX = [0] * n
        lastLineY = [0] * n

        ans = 0

        for i in range(m):
            lineX = []
            lineY = []
            preX = [0]
            preY = [0]

            for j in range(n):
                if(grid[i][j] == 'X'):
                    preX.append(preX[-1] + 1)
                    preY.append(preY[-1])
                if(grid[i][j] == 'Y'):
                    preX.append(preX[-1])
                    preY.append(preY[-1] + 1)
                lineX.append(lastLineX[j] + preX[-1])
                lineY.append(lastLineY[j] + preY[-1])

                if(lineX[-1] != 0 and lineX[-1] == lineY[-1]):
                    ans += 1

            lastLineX = lineX
            lastLineY = lineY
        
        return ans