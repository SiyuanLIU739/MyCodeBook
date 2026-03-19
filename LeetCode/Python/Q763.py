class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}

        for i in range(len(s)):
            if(s[i] not in first.keys()):
                first[s[i]] = i
            last[s[i]] = i

        ans = []

        left = -1
        right = -1
        for i in range(len(s)):
            right = max(right, last[s[i]])
            if(i == right):
                ans.append(right - left)
                left = i
                right = i
        
        return ans