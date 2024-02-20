class Solution:
    def numWays(self, n: int, k: int) -> int:
        sum = [k]

        f = []
        f.append([1] * k)

        for i in range(1, n):
            f.append([0] * k)
            sum.append(0)

            for j in range(k):
                f[i][j] = sum[i - 1] - f[i - 1][j]

                if(i > 1):
                    f[i][j] += (sum[i - 2] - f[i - 2][j])

                sum[i] += f[i][j]

        ans = sum[-1]
        if(len(sum) > 1):
            ans += sum[-2]
        
        return ans
