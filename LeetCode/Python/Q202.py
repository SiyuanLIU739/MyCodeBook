class Solution:
    def isHappy(self, n: int) -> bool:
        meet = {n}

        while(n != 1):
            sum_sqrt = 0
            while(n > 0):
                sum_sqrt += (n % 10) ** 2
                n = n // 10
            n = sum_sqrt

            if(n in meet):
                return False
            
            meet.add(n)

        return True
        