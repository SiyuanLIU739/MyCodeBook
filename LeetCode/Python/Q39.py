from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        f = [[] for i in range(target + 1)]
        f[0].append([])

        candidates.sort()

        for candidate in candidates:
            for i in range(1, target + 1):
                if(i - candidate < 0):
                    continue

                for p in f[i - candidate]:
                    t = p.copy()
                    t.append(candidate)
                    f[i].append(t)

        return f[target]