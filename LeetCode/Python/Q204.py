class Solution:
    def countPrimes(self, n: int) -> int:
        nonPrime = [False] * (n + 1)

        if(n <= 2):
            return 0
        
        cnt = 0
        for i in range(2, n):
            if(nonPrime[i]):
                continue
            cnt += 1
            for j in range(2, n):
                if(i * j > n):
                    break
                nonPrime[i * j] = True

        return cnt