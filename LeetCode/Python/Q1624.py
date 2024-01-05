class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        record = {}
        for i in range(len(s)):
            if(s[i] in record.keys()):
                ans = max(ans, i - record[s[i]] - 1)
            else:
                record[s[i]] = i
        
        return ans