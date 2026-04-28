class Solution:
    def convertToBase7(self, num: int) -> str:
        if(num == 0):
            return '0'

        ans = ""
        sign = ""
        if(num < 0):
            num = -num
            sign = '-'

        while(num != 0):
            ans = str(num % 7) + ans
            num = num // 7

        ans = sign + ans
        
        return ans 