class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        mappingt = {}

        for i in range(len(s)):
            if(s[i] not in mappings.keys() and t[i] not in mappingt.keys()):
                mappings[s[i]] = t[i]
                mappingt[t[i]] = s[i]
            elif(s[i] in mappings.keys() and t[i] in mappingt.keys()):
                if(mappings[s[i]] != t[i] or mappingt[t[i]] != s[i]):
                    return False
            else:
                return False
            
        return True