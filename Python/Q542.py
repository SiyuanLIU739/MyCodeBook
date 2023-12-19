from ast import List
from queue import PriorityQueue


class points:
    def __init__(self, line, column, dist):
        self.line = line
        self.col = column
        self.dist = dist
    
    def __lt__(self, other):
        return self.dist < other.dist
    

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = []

        n = len(mat)
        m = len(mat[0])

        
        q = PriorityQueue()

        maxN = 10000
        for i in range(n):
            init = []
            
            for j in range(m):
                if(mat[i][j] == 0):
                    init.append(0)
                    q.put(points(i, j, 0))
                else:
                    init.append(maxN)

            ans.append(init)

        dl = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        while(not q.empty()):
            p = q.get()

            l = p.line
            c = p.col
            dist = p.dist

            for i in range(4):
                ll = l + dl[i]
                cc = c + dc[i]

                if((ll < 0) or (ll >= n) or (cc < 0) or (cc >= m) or (ans[ll][cc] <= (dist + 1))):
                    continue

                ans[ll][cc] = dist + 1

                q.put(points(ll, cc, dist + 1))

        return ans