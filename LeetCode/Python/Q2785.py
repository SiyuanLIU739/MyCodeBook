class Solution:
    def sortVowels(self, s: str) -> str:
        t = ""

        for char in s:
            if(char in "AEIOUaeiou"):
                t = t + char

        t = sorted(t)

        i = 0
        j = 0

        while(i < len(t)):
            if(s[j] in "AEIOUaeiou"):
                s = s[: j] + t[i] + s[j + 1: ]
                i += 1
            j += 1

        return s