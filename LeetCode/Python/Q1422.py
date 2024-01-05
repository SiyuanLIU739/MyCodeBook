class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            if(i == 0):
                if(s[i] == '0'):
                    ans += 1
            else:
                if(s[i] == '1'):
                    ans += 1

        lastx = ans
        for i in range(1, len(s) - 1):
            x = lastx
            if(s[i] == '1'):
                x -= 1
            else:
                x += 1
            ans = max(ans, x)
            lastx = x
        
        return ans