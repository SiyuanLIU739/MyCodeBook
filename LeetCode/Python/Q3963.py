class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = [['#'] * n for i in range(m)]

        for i in range(n):
            ans[0][i] = '.'

        for i in range(m):
            ans[i][-1] = '.'
        
        ret = []
        for i in range(m):
            ret.append("".join(ans[i]))

        return ret