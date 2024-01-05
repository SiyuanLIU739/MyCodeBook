class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        ans = []
        for i in range(m):
            lst = [0] * n
            ans.append(lst)

        delta = [-1, 0, 1]
        X = range(m)
        Y = range(n)
        for i in range(m):
            for j in range(n):
                count = 0
                for xx in delta:
                    for yy in delta:
                        x = i + xx
                        y = j + yy
                        if(x in X and y in Y):
                            ans[i][j] += img[x][y]
                            count += 1

                ans[i][j] = ans[i][j] // count

        return ans