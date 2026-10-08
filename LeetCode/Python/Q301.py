class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0
        right = 0
        left_loc = []
        right_loc = []

        for i in range(len(s)):
            char = s[i]
            if(char == '('):
                left += 1
                left_loc.append(i)
            elif(char == ')'):
                right_loc.append(i)
                if(left > 0):
                    left -= 1
                else:
                    right += 1

        def valid(p):
            left = 0
            for char in p:
                if(char == '('):
                    left += 1
                elif(char == ')'):
                    if(left > 0):
                        left -= 1
                    else:
                        return False
            if(left == 0):
                return True
            return False

        ans = set()

        from itertools import combinations
        for left_comb in combinations(left_loc, left):
            for right_comb in combinations(right_loc, right):
                pending = ""
                for i in range(len(s)):
                    if(i in left_comb or i in right_comb):
                        continue
                    pending += s[i]
                if(valid(pending)):
                    ans.add(pending)

        return list(ans)