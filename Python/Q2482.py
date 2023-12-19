class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        r = []
        for i in range(m):
            r.append(0)
        c = []
        for i in range(n):
            c.append(0)

        for i in range(m):
            for j in range(n):
                r[i] += grid[i][j]
                c[j] += grid[i][j]

        ans = []
        for i in range(m):
            lst = []
            for j in range(n):
                lst.append(2 * (r[i] + c[j]) - m - n)
            ans.append(lst)

        return ans 