class Solution:
    def numSpecial(self, mat) -> int:
        f = []
        h = []

        m = len(mat)
        n = len(mat[0])

        lstf = [mat[0][0]]
        lsth = [mat[0][0]]
        for j in range(1, n):
            lstf.append(lstf[j - 1] + mat[0][j])
            lsth.append(mat[0][j])
        f.append(lstf)
        h.append(lsth)

        for i in range(1, m):
            lstf = [mat[i][0]]
            lsth = [h[i - 1][0] + mat[i][0]]
            for j in range(1, n):
                lstf.append(lstf[j - 1] + mat[i][j])
                lsth.append(h[i - 1][j] + mat[i][j])
            f.append(lstf)
            h.append(lsth)

        ans = 0
        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 0):
                    continue
                if((f[i][j] == 1) and (f[i][n - 1] == 1) and (h[i][j] == 1) and (h[m - 1][j] == 1)):
                    ans += 1

        return ans

            