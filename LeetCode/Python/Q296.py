class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x = []
        y = []

        m = len(grid)
        n = len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    x.append(i)
                    y.append(j)
                    count += 1

        x = sorted(x)
        y = sorted(y)

        posx = x[int((count + 1) / 2) - 1]
        posy = y[int((count + 1) / 2) - 1]

        ans = 0
        for i in range(count):
            ans += abs(x[i] - posx)
            ans += abs(y[i] - posy)

        return ans