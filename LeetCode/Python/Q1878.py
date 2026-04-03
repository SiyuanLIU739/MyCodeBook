class Solution:
    def edgeCheck(self, i, j, m, n, size):
        # upper corner
        a = i - size
        b = j + size
        if(a < 0 or b >= n):
            return False
        
        # right corner
        a = i
        b = b + size
        if(b >= n):
            return False
        
        # lower corner
        a = i + size
        b = j + size

        if(a >= m or b >= n):
            return False
        
        return True
    
    
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        extend = min(m, n) // 2

        ans = [0, 0, 0]
        for i in range(0, m):
            for j in range(0, n):
                for size in range(extend, -1, -1):
                    if(self.edgeCheck(i, j, m, n, size)):
                        sumEdge = 0
                        if(size == 0):
                            sumEdge = grid[i][j]
                        else:
                            # go right up
                            for s in range(0, size):
                                loci = i - s
                                locj = j + s
                                sumEdge += grid[loci][locj]
                            # go right down
                            i = i - size
                            j = j + size
                            for s in range(0, size):
                                loci = i + s
                                locj = j + s
                                sumEdge += grid[loci][locj]
                            # go left down
                            i = i + size
                            j = j + size
                            for s in range(0, size):
                                loci = i + s
                                locj = j - s
                                sumEdge += grid[loci][locj]
                            # go left up
                            i = i + size
                            j = j - size
                            for s in range(0, size):
                                loci = i - s
                                locj = j - s
                                sumEdge += grid[loci][locj]
                            
                            # go back
                            i = i - size
                            j = j - size
                        
                        if(sumEdge not in ans):
                            if(sumEdge > ans[0]):
                                ans[2] = ans[1]
                                ans[1] = ans[0]
                                ans[0] = sumEdge
                            elif(sumEdge > ans[1]):
                                ans[2] = ans[1]
                                ans[1] = sumEdge
                            elif(sumEdge > ans[2]):
                                ans[2] = sumEdge

        ret = []
        for i in range(3):
            if(ans[i] != 0):
                ret.append(ans[i])

        return ret