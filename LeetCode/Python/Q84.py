class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights = [-1] + heights + [-1]

        leftbound = [-1]
        stack = [0]
        for i in range(1, n + 1):
            while(heights[stack[-1]] >= heights[i]):
                stack.pop()
            leftbound.append(stack[-1])
            stack.append(i)

        rightbound = [-1]
        stack = [n + 1]
        for i in range(n, 0, -1):
            while(heights[stack[-1]] >= heights[i]):
                stack.pop()
            rightbound.append(stack[-1])
            stack.append(i)
        rightbound.reverse()
        rightbound = [-1] + rightbound
        
        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, (rightbound[i] - leftbound[i] - 1) * heights[i])

        return ans