class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "A" + word1
        word2 = "B" + word2

        f = []
        inf = 10000
        for i in range(len(word1)):
            lst = []
            for j in range(len(word2)):
                lst.append(inf)

            f.append(lst)
        
        f[0][0] = 0

        for i in range(len(word1)):
            for j in range(len(word2)):
                if(word1[i] != word2[j]):
                    if(i - 1 >= 0):
                        f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                    if(j - 1 >= 0):
                        f[i][j] = min(f[i][j], f[i][j - 1] + 1)
                    if((i - 1 >= 0) and (j - 1 >= 0)):
                        f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)

                else:
                    f[i][j] = f[i - 1][j - 1]

        return f[len(word1) - 1][len(word2) - 1]
    
    