class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.matches(n)

    def matches(self, n):
        if(n == 1):
            return 0
            
        if(n == 2):
            return 1
        
        ans = 0
        if(n % 2 == 1):
            ans = (n - 1) / 2
            ans += self.matches((n + 1) / 2)

        else:
            ans = n / 2
            ans += self.matches(n / 2)

        return int(ans)