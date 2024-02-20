class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if(n > m):
            return ""
        
        if(n == 1):
            if(t in s):
                return t
            return ""
        
        charS = {}
        charT = {}
        self.countChar(t, charT)
        notSatisfied = list(set(t))

        l = 0
        r = -1
        minl = m + 1
        ans = ""

        while(r < m):
            while(len(notSatisfied) != 0):
                r += 1
                if(r >= m):
                    break

                if(s[r] not in charS.keys()):
                    charS[s[r]] = 0
                charS[s[r]] += 1

                if(s[r] in notSatisfied and charS[s[r]] >= charT[s[r]]):
                    notSatisfied.remove(s[r])
                
                if(len(notSatisfied) == 0):
                    break
            
            while(len(notSatisfied) == 0):
                if(r - l + 1 < minl):
                    minl = r - l + 1
                    ans = s[l: r + 1]

                charS[s[l]] -= 1
                if(s[l] in t and charS[s[l]] < charT[s[l]]):
                    notSatisfied.append(s[l])

                l += 1
        
        return ans      

    def countChar(self, s, charS):
        for char in s:
            if(char not in charS.keys()):
                charS[char] = 0
            charS[char] += 1