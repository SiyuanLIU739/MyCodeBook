class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1odd = []
        s1even = []
        s2odd = []
        s2even = []

        n = len(s1)
        for i in range(n):
            if(i % 2 == 0):
                s1even.append(s1[i])
                s2even.append(s2[i])
            else:
                s1odd.append(s1[i])
                s2odd.append(s2[i])

        s1even.sort()
        s2even.sort()
        s1odd.sort()
        s2odd.sort()

        for i in range(len(s1even)):
            if(s1even[i] != s2even[i]):
                return False
        for i in range(len(s2odd)):
            if(s1odd[i] != s2odd[i]):
                return False
            
        return True