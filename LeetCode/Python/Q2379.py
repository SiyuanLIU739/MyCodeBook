class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        f = []
        ans = 10086

        l = len(blocks)

        for i in range(l):
            f.append([10086] * (k + 1))
            f[-1][0] = 0
        if(blocks[0] == 'W'):
            f[0][1] = 1
        else:
            f[0][1] = 0

        for i in range(1, l):
            for j in range(min(i + 1, k)):
                f[i][j + 1] = f[i - 1][j]

                if(blocks[i] == 'W'):
                    f[i][j + 1] += 1

        for i in range(l):
            ans = min(ans, f[i][k])

        return ans