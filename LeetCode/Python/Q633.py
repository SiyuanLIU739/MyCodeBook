class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if(c == 0):
            return True
        
        r = int(sqrt(c)) + 1

        for i in range(r):
            while(r ** 2 + i ** 2 > c):
                r -= 1
            if(r ** 2 + i ** 2 == c):
                return True
        
        return False