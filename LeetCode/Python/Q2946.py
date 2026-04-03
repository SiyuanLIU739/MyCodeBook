class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        k = k % n

        if(k == 0):
            return True
        
        matp = []
        for i in range(m):
            matp.append(mat[i].copy())

        for i in range(k):
            for row in range(m):
                if(row % 2 == 0):
                    num = matp[row].pop(0)
                    matp[row].append(num)
                else:
                    num = matp[row].pop(-1)
                    matp[row].insert(0, num)

        for i in range(m):
            for j in range(n):
                if(mat[i][j] != matp[i][j]):
                    return False
                

        return True