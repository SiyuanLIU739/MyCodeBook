class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        
        f = [1]
        for i in range(target):
            f.append(0)

        for i in range(1, n + 1):
            for j in range(min(target, i * k), i - 1, -1):
                f[j] = 0
                for t in range(1, k + 1):
                    if(j - t < i - 1):
                        break
                    f[j] += f[j - k]
                    f[j] %= mod
            
        return f[target]
