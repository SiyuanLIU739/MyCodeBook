class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0] * (n + 1) for i in range(m + 1)]

        ans = 0
        for str in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    n0, n1 = self.countNum(str)
                    if(i >= n0 and j >= n1):
                        f[i][j] = max(f[i][j], f[i - n0][j - n1] + 1)
                    ans = max(ans, f[i][j])

        return ans
    
    def countNum(self, str):
        n0 = 0
        n1 = 0

        for char in str:
            if(char == '0'):
                n0 += 1
            else:
                n1 += 1

        return (n0, n1)