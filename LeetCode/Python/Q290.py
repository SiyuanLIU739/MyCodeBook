class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterntos = {}
        stopattern = {}

        words = s.split(" ")

        if(len(words) != len(pattern)):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if(char not in patterntos.keys() and word not in stopattern.keys()):
                patterntos[char] = word
                stopattern[word] = char

            elif(char not in patterntos.keys() or word not in stopattern.keys()):
                return False
            
            else:
                if(word != patterntos[char] or stopattern[word] != char):
                    return False
                
        return True