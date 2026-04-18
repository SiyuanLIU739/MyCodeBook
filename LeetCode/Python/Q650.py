class Solution:
    def minSteps(self, n: int) -> int:
        f = [100000] * (n + 1)

        f[1] = 0

        for i in range(n + 1):
            for j in range(1, i):
                if(i % j == 0):
                    f[i] = min(f[i], f[j] + i // j)

        return f[n]