class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        balanced = []
        n = len(s)

        for i in range(1, n):
            if(s[i - 1] == '(' and s[i] == ')'):
                balanced.append((i - 1, i, 1))

        while(len(balanced) != 1 or not (balanced[0][0] == 0 and balanced[0][1] == (n - 1))):
            extended = []
            for par in balanced:
                l = par[0]
                r = par[1]
                score = par[2]

                if(l == 0 or r == (n - 1)):
                    extended.append((l, r, score))
                    continue

                while(l != 0 and r != (n - 1) and (s[l - 1] == '(' and s[r + 1] == ')')):
                    l -= 1
                    r += 1
                    score *= 2

                extended.append((l, r, score))

            extended.sort()
            balanced = []
            l = extended[0][0]
            r = extended[0][1]
            score = extended[0][2]
            for i in range(1, len(extended)):
                par = extended[i]
                if(r + 1 == par[0]):
                    r = par[1]
                    score += par[2]

                else:
                    balanced.append((l, r, score))
                    l = par[0]
                    r = par[1]
                    score = par[2]

            balanced.append((l, r, score))

        return balanced[0][2]