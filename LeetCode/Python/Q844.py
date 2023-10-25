class Solution:
    def backspaceCompare2(self, s: str, t: str) -> bool:
        ss = []
        tt = []

        for c in s:
            if(c == '#'):
                ss.pop(-1)
            else:
                ss.append(c)
        
        for c in t:
            if(c == '#'):
                tt.pop(-1)
            else:
                tt.append(c)

        if(len(ss) != len(tt)):
            return False
        
        for i in range(len(tt)):
            if(ss[i] != tt[i]):
                return False
            
        return True
    


    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = 1
        tt = 1

        while(True):
            (ss, sN) = self.nextChar(s, ss)
            (tt, tN) = self.nextChar(t, tt)

            if(sN != tN):
                return False
            
            if("F" in [sN, tN]):
                return sN == tN
            
    def nextChar(self, s: str, index: int) -> (int, str):
        if(index > len(s)):
            return (index + 1, "F")
        
        while(True):
            if(s[-index] != '#'):
                return (index + 1, s[-index])
            
            hashSign = 1
            index += 1
            while(hashSign > 0):
                if(index > len(s)):
                    return (index + 1, "F")
                
                if(s[-index] == '#'):
                    hashSign += 1
                else:
                    hashSign -= 1
                index += 1

            if(index > len(s)):
                return (index + 1, "F")
    
sol = Solution()
s = "ab#c"
t = "ad#c"
print(sol.backspaceCompare(s, t))