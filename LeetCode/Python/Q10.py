class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = '0' + s
        
        pList = ['0']
        for char in p:
            if(char == '*'):
                pList[-1] = pList[-1] + '*'
            else:
                pList.append(char)
        p = pList

        f = [[False] * len(p) for i in range(len(s))]
        f[0][0] = True

        for i in range(0, len(s)):
            for j in range(1, len(p)):
                if(len(p[j]) == 2):
                    f[i][j] = f[i][j - 1]
                    if(p[j][0] == '.' or p[j][0] == s[i]):
                        f[i][j] = f[i][j] or f[i - 1][j - 1] or f[i - 1][j]
                else:
                    if(s[i] == p[j] or p[j] == '.'):
                        f[i][j] = f[i - 1][j - 1]
        print(f)
        return f[len(s) - 1][len(p) - 1]