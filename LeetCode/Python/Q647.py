class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            l = r = i
            while(l >= 0 and r < n):
                if(s[l] == s[r]):
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

            l = i
            r = i + 1
            while(l >= 0 and r < n):
                if(s[l] == s[r]):
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

        return ans