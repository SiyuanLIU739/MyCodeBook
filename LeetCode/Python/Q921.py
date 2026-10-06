class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = 0
        ans = 0

        for char in s:
            if(char == '('):
                left_count += 1
            else:
                if(left_count == 0):
                    ans += 1
                else:
                    left_count -= 1

        return ans + left_count