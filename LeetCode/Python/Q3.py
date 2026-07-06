class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 256

        l = 0
        ans = 0
        for r in range(len(s)):
            c = s[r]

            l = max(l, last_seen[ord(c)] + 1)

            ans = max(ans, r - l + 1)

            last_seen[ord(c)] = r

        return ans