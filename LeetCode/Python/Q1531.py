class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        f = []
        h = []

        n = len(s)
        inf = n * 2
        s = 'A' + s

        for i in range(n + 1):
            lst = []
            l = []
            for j in range(k + 1):
                lst.append([inf] * 26)
                l.append([0] * 26)
            f.append(lst)
            h.append(l)

        for i in range(26):
            f[0][0][i] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                char = ord(s[i]) - ord('a')
                c = char
                # the desired end of the str is s[i]
                if(h[i - 1][j][char] <= 1):
                    f[i][j][char] = f[i - 1][j][char] + 1
                    h[i][j][char] = h[i - 1][j][char] + 1
                else:
                    h[i][j][char] = h[i - 1][j][char] + 1
                    f[i][j][char] = f[i - 1][j][char] - len(str(h[i - 1][j][char])) + len(str(h[i][j][char]))

                for char in range(26):
                    # delete ith char
                    if(j > 0):
                        if(f[i][j][char] > f[i - 1][j - 1][char]):
                            f[i][j][char] = f[i - 1][j - 1][char]
                            h[i][j][char] = h[i - 1][j - 1][char]

                    if(char != c):
                        if(f[i][j][c] > f[i - 1][j][char] + 1):
                            f[i][j][c] = f[i - 1][j][char] + 1
                            h[i][j][c] = 1
                            
        ans = inf
        for i in range(26):
            ans = min(ans, f[n][k][i])
        return ans