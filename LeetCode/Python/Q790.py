class Solution:
    def numTilings(self, n: int) -> int:
        self.mod = 1000000007

        self.f = []
        for i in range(n + 1):
            lst = [0] * (n + 1)
            self.f.append(lst)

        self.f[0][0] = 1

        return self.dp(n, n)
    
    def dp(self, i, j):
        if((i < 0) or (j < 0)):
            return 0
        
        if(self.f[i][j] != 0):
            return self.f[i][j]

        ans = 0

        if(i == j):
            for x in [1, 2]:
                for y in [1, 2]:
                    ans = (ans + self.dp(i - x, j - y)) % self.mod
        
        elif(j - i == 1):
            for x in [0, 1]:
                ans = (ans + self.dp(i - x, j - 2)) % self.mod

        elif(i - j == 1):
            for y in [0, 1]:
                ans = (ans + self.dp(i - 2, j - y)) % self.mod
        
        elif(i - j >= 2):
            ans = self.dp(i - 2, j)

        else:
            ans = self.dp(i, j - 2)

        self.f[i][j] = ans
        return ans