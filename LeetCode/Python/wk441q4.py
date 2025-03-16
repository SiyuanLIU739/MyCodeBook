class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        ans = 0
        for x in range(l, r + 1):
            if(self.checkx(x)):
                ans += 1

        return ans
    
    def checkx(x):
        sum = 0
        prod = 1

        while(x > 0):
            digit = x % 10
            x = x // 10
            if(digit == 0):
                return True
            
            sum += digit
            prod *= digit

        return prod % sum == 0