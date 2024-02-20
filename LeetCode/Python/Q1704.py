class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        a = s[: n // 2]
        b = s[n // 2: ]

        cnta = 0
        for char in a:
            if(char in 'AEIOUaeiou'):
                cnta += 1

        cntb = 0
        for char in b:
            if(char in 'AEIOUaeiou'):
                cntb += 1
        
        return cnta == cntb