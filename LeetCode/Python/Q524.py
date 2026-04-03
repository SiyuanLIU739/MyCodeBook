class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x), x))
        
        for word in dictionary:
            sp = 0
            for i in range(len(word)):
                while(sp < len(s)):
                    if(s[sp] != word[i]):
                        sp += 1
                    else:
                        break
                if(sp == len(s)):
                    break
                if(word[i] == s[sp] and i != len(word) - 1):
                    sp += 1
            if(sp != len(s)):
                return word

        return ""