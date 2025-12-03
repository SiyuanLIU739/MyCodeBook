class Solution:
    def isPalindrome(self, s: str) -> bool:
        sprime = ''
        s = s.lower()

        for char in s:
            if char in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                sprime = sprime + char

        l = 0
        r = len(sprime) - 1
        while(l < r):
            if(sprime[l] != sprime[r]):
                return False
            
            l += 1
            r -= 1

        return True