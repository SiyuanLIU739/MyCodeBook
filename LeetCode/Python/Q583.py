class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = '0' + word1
        word2 = '1' + word2

        f = [[1001] * len(word2) for i in range(len(word1))]
        f[0][0] = 0
        
        for i in range(0, len(word1)):
            for j in range(0, len(word2)):
                if(word1[i] == word2[j]):
                    f[i][j] = f[i - 1][j - 1]
                else:
                    if(i != 0):
                        f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                    if(j != 0):
                        f[i][j] = min(f[i][j], f[i][j - 1] + 1)

        return f[len(word1) - 1][len(word2) - 1] 