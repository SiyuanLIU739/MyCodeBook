class Solution:
    def reverse(self, x: int) -> int:
        signed = False

        if(x < 0):
            x = -x
            signed = True

        ans = 0
        while(x > 0):
            ans = ans * 10 + (x % 10)
            x = x // 10

        if(ans > 2147483648):
            ans = 0

        if(not signed and ans == 2147483648):
            ans = 0

        if(signed):
            ans = -ans

        return ans