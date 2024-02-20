class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countss = self.countchar(s)
        countst = self.countchar(t)

        count = 0
        for char, c in countss.items():
            if (char in countst.keys()):
                count += min(c, countst[char])

        return len(s) - count

    def countchar(self, s):
        counts = {}

        for char in s:
            if(char in counts.keys()):
                counts[char] += 1
            else:
                counts[char] = 1

        return counts