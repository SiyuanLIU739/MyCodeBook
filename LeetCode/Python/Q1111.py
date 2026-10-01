class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack = [0]
        depths = []
        max_depth = 0

        for char in seq:
            if(char == '('):
                stack.append(stack[-1] + 1)
                depths.append(stack[-1])
                max_depth = max(max_depth, stack[-1])

            else:
                last = stack.pop()
                depths.append(last)

        target = (max_depth + 1) // 2
        ans = []

        for depth in depths:
            if(depth <= target):
                ans.append(0)
            else:
                ans.append(1)

        return ans