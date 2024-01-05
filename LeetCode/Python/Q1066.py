class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.m = len(bikes)
        self.n = len(workers)
        self.bikes = bikes
        self.workers = workers

        self.f = {(0, 0): 0}

        self.ans = 1000 * 2 * 10 + 5
        self.inf = 1000 * 2 * 10 + 5

        self.comb(0, [])

        return self.ans
    
    def comb(self, j, c):
        if(len(c) == self.n):
            self.ans = min(self.ans, self.dp(self.n, c))
            return
        
        if(j == self.m):
            return
        if(self.m - j < self.n - len(c)):
            return
        
        self.comb(j + 1, c)
        c.append(j)
        self.comb(j + 1, c)
        c.remove(j)

    def dp(self, i, j):
        hashj = self.hash(j)
        if((i, hashj) in self.f.keys()):
            return self.f[(i, hashj)]
        
        ans = self.inf
        lst = j.copy()
        for k in j:
            lst.remove(k)
            ans = min(ans, self.dp(i - 1, lst) + self.dist(self.workers[i - 1], self.bikes[k]))
            lst.append(k)

        self.f[(i, hashj)] = ans
        return ans

    def dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def hash(self, lst):
        ans = 0

        for k in lst:
            ans += (2 ** k)

        return ans