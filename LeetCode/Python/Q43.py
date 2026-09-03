class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num2)

        adds = []
        for i in range(n):
            adds.append(self.multiply_single(num1, num2[i]) + '0' * (n - i - 1))

        ans = '0'
        for add in adds:
            ans = self.plus(ans, add)

        for i in range(len(ans)):
            if(ans[i] != '0'):
                return ans[i: ]
                
        return '0'

    def multiply_single(self, num1, num):
        ans = ""
        rem = 0

        for i in range(len(num1) - 1, -1, -1):
            tem = int(num1[i]) * int(num) + rem
            ans = str(tem % 10) + ans
            rem = tem // 10

        if(rem > 0):
            ans = str(rem) + ans

        return ans

    def plus(self, a, b):
        if(len(a) < len(b)):
            c = b
            b = a
            a = c

        b = '0' * (len(a) - len(b)) + b

        ans = ""

        rem = 0
        for i in range(len(a) - 1, -1, -1):
            tem = int(a[i]) + int(b[i]) + rem
            ans = str(tem % 10) + ans
            rem = tem // 10

        if(rem > 0):
            ans = str(rem) + ans

        return ans