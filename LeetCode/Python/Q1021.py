class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        last = -1

        lefts = []
        for i in range(len(s)):
            if(s[i] == '('):
                lefts.append(i)
            else:
                left = lefts.pop()
                if(left == last + 1):
                    ans += s[left + 1: i]
                    last = i

        return ans