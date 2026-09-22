class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            ch = s[i]

            rev = 26 - ord(ch) + ord('a')

            ans += (ch * (i + 1))

        return ans