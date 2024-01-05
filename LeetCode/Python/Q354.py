class Doll:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __lt__(self, other):
        if(self.x == other.x):
            return self.y > other.y
        return self.x < other.x

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dolls = []

        for env in envelopes:
            dolls.append(Doll(env[0], env[1]))

        dolls.sort()

        ans = [100001]
        for i in range(len(dolls)):
            if(dolls[i].y <= ans[-1]):
                k = self.bs(ans, 0, len(ans) - 1, dolls[i].y)
                ans[k] = dolls[i].y
            else:
                ans.append(dolls[i].y)

        return len(ans)
    
    def bs(self, lst, l, r, target):
        if(lst[l] >= target):
            return l
        if(lst[r] < target):
            return r + 1
        
        mid = int((l + r) / 2)

        if(lst[mid] == target):
            return mid
        if(lst[mid] < target):
            return self.bs(lst, mid + 1, r, target)
        return self.bs(lst, l, mid, target)