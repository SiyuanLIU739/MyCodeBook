class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        self.dfs(0, n, "")

        return self.ans


    def dfs(self, unmatched, left, s):
        if(unmatched == 0 and left == 0):
            self.ans.append(s)

        if(unmatched > 0):
            self.dfs(unmatched - 1, left, s + ')')

        if(left > 0):
            self.dfs(unmatched + 1, left - 1, s + '(')