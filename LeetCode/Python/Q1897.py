class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        rec = {}
        n = len(words)

        for i in range(n):
            for char in words[i]:
                if(char in rec.keys()):
                    rec[char] += 1
                else:
                    rec[char] = 1
        
        for key in rec.keys():
            if(rec[key] % n != 0):
                return False
        
        return True