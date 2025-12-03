class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        
        s = ""
        while(x > 0):
            s += str(x % 10)
            x = x // 10

        l = 0
        r = len(s) - 1
        while(l < r):
            if(s[l] != s[r]):
                return False
            l += 1
            r -= 1

        return True