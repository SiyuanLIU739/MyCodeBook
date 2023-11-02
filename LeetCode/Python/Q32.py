class Solution:
    def longestValidParentheses(self, s: str) -> int:
        parenthesis = []
        index = []

        for i in range(len(s)):
            if(s[i] == '('):
                parenthesis.push('(')
                index.push(i)
            else:
                # try to match
                last = ('' if (len(parenthesis) == 0) else parenthesis[-1])
                if(last == '('):
                    parenthesis.pop()
                    index.pop()
                else:
                    parenthesis.push(')')
                    index.push(i)

        ans = 0
        last = len(s)

        while(len(index) != 0):
            now = index[-1]
            index.pop()
            ans = max(ans, last - now - 1)
            last = now

        return ans