class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(101, 0)]

        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            while(temperatures[i] >= stack[-1][0]):
                stack.pop()

            ans.append(max(0, stack[-1][1] - i))
            stack.append((temperatures[i], i))

        ans = ans.reverse()
        return ans