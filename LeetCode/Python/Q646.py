class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1], -x[0]))
        pairs = [[-2000, -1999]] + pairs
        
        ans = 0
        
        f = [0] * len(pairs)

        for i in range(1, len(pairs)):
            for j in range(i):
                if(pairs[j][1] >= pairs[i][0]):
                    break
                f[i] = max(f[i], f[j] + 1)
            ans = max(f[i], ans)

        return ans