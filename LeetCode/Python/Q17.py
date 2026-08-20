class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []

        self.dfs(digits, 0, "")

        return self.ans

    def dfs(self, digits, i, s):
        if(i == len(digits)):
            self.ans.append(s)
            return

        char_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxzy'
        }

        for ch in char_map[digits[i]]:
            self.dfs(digits, i + 1, s + ch)