class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        count = {}
        
        for char in s:
            if(char not in count.keys()):
                count[char] = 0
            count[char] += 1

        for char in t:
            if(char not in count.keys()):
                return False
            
            if(count[char] == 0):
                return False
            
            count[char] -= 1

        return True