class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        inf = 300 * 1000 * 2

        
        n = len(jobDifficulty)

        if(n < d):
            return -1

        f = [[0]]
        jobDifficulty.insert(0, 0)

        for i in range(1, n + 1):
            f.append([inf])
            for j in range(1, min(i, d) + 1):
                s = 0
                f[-1].append(inf)
                for k in range(i - 1, j - 2, -1):
                    s = max(s, jobDifficulty[k + 1])
                    f[-1][-1] = min(f[-1][-1],  f[k][j - 1] + s)

        return f[n][d]