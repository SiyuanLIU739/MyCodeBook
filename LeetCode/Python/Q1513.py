class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        first1 = 0
        for j in range(len(s)):
            if(s[j] == '0'):
                first1 = j + 1
            else:
                ans += (j - first1 + 1)
                ans = ans % (10 ** 9 + 7)

        return ans