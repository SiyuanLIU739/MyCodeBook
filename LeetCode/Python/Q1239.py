class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = []
        queue = []

        for a in arr:
            seta = set(a)
            if(len(seta) != len(a)):
                continue
            charSet.append(seta)
        
        queue.append(set())
        if(len(charSet) == 0):
            return 0
        queue.append(charSet[0])
            

        ans = len(charSet[0])
        for i in range(1, len(charSet)):
            for j in range(len(queue)):
                if(len(charSet[i] & queue[j]) == 0):
                    comb = charSet[i] | queue[j]
                    queue.append(comb)
                    ans = max(ans, len(comb))
                    
        return ans