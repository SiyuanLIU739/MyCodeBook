class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = []
        btrust = []

        for i in range(n + 1):
            trusts.append([])
            btrust.append([])

        for t in trust:
            trusts[t[0]].append(t[1])
            btrust[t[1]].append(t[0])

        for i in range(1, n + 1):
            if(len(btrust[i]) == n - 1):
                if(len(trusts[i]) == 0):
                    return i
                
        return -1
