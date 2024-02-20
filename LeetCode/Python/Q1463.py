class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        inf = 100*70*70*2
        f = [[]]
        for i in range(n):
            f[0].append([-inf] * n)
            
        f[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
        steps = [-1, 0, 1]

        ans = 0
        for i in range(1, m):
            print(f[-1])
            f.append([])
            for j in range(n):
                f[i].append([-inf] * n)

            for j in range(0, n):
                for k in range(0, n):
                    for jj in steps:
                        if(j + jj < 0 or j + jj >= n):
                            continue
                        for kk in steps:
                            if(k + kk < 0 or k + kk >= n):
                                continue
                            f[i][j][k] = max(f[i][j][k], f[i - 1][j + jj][k + kk])
                    
                    if(j == k):
                        f[i][j][k] = f[i][j][k] + grid[i][j]
                    else:
                        f[i][j][k] = f[i][j][k] + grid[i][j] + grid[i][k]

                    ans = max(ans, f[i][j][k])


        return ans