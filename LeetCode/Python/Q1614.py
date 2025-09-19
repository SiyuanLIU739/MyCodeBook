class Solution:
    def maxDepth(self, s: str) -> int:
        l = 0
        maxL = 0

        for char in s:
            if(char == '('):
                l += 1
                maxL = max(l, maxL)

            if(char == ')'):
                l -= 1

        return maxL