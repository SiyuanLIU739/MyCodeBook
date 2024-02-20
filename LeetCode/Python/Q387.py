class Solution:
    def firstUniqChar(self, s: str) -> int:
        happened = []

        for i in range(len(s)):
            if(s[i] in happened):
                continue

            if(s[i] not in s[i + 1:]):
                return i
            
            happened.append(s[i])

        return -1