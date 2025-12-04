class Solution:
    def divisorGame(self, n: int) -> bool:
        f = [False, False, True, False]

        if(n <= 3):
            return f[n]
        
        for i in range(4, n + 1):
            divisors = [1]
            j = 2
            m = i ** (1 / 2)
            while(j < m):
                if(i % j == 0):
                    divisors.append(j)
                    divisors.append(i // j)
                j += 1
            
            f.append(False)
            for divisor in divisors:
                if(f[i - divisor] == False):
                    f[-1] = True
                    break
            
        return f[n]