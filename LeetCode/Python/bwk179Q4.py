class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        n = len(digitSum)

        f = [[0] * 5001 for i in range(n)]
        ds = [-1] * 5001

        for j in range(5001):
            ds[j] = self.calDigitSum(j)
            if(j != 0):
                f[0][j] = f[0][j - 1]
            if(ds[j] == digitSum[0]):
                f[0][j] += 1

        for i in range(1, n):
            for j in range(5001):
                if(j != 0):
                    f[i][j] = f[i][j - 1]
                if(ds[j] == digitSum[i]):
                    f[i][j] += f[i - 1][j]

                f[i][j] = f[i][j] % (1000000000 + 7)

        return f[n - 1][5000]
        
    def calDigitSum(self, x):
        ret = 0

        while(x != 0):
            ret += (x % 10)
            x = x // 10

        return ret
    
sol = Solution()
digitSum = [14,9,15,19,23]
print(sol.countArrays(digitSum))