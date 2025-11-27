class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countmagazine = {}
        for char in magazine:
            if(char not in countmagazine.keys()):
                countmagazine[char] = 0
            countmagazine[char] += 1

        for char in ransomNote:
            if(char not in countmagazine.keys() or countmagazine[char] <= 0):
                return False
            countmagazine[char] -= 1

        return True