class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        self.comb(n + 1, k, set(), 0)

        return self.ans
    
    def comb(self, n, k, chosen, m):
        if(len(chosen) == k):
            self.ans.append(list(chosen))
            return
        
        for i in range(m + 1, n):
            if(i in chosen):
                continue
            chosen.add(i)
            self.comb(n, k, chosen, i)
            chosen.remove(i)