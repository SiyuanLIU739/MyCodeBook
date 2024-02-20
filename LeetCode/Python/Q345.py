class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []

        for char in s:
            if char in 'aeiouAEIOU':
                lst.append(char)
        
        for i in range(len(s)):
            if(s[i] in 'aeiouAEIOU'):
                s = s[: i] + lst[-1] + s[i + 1:]
                lst.pop()

        return s