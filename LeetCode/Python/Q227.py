class Solution:
    def calculate(self, s: str) -> int:
        sp = ""
        for char in s:
            if char != ' ':
                sp += char

        last = ""
        exp = []
        for char in sp:
            if(char in '+-*/'):
                exp.append(int(last))
                exp.append(char)
            else:
                last += char
        exp.append(int(last))

        low_priority = []
        i = 0
        n = len(exp)
        while(i < n):
            v = exp[i]
            if(v == '*'):
                v1 = exp[i + 1]
                v2 = low_priority.pop()
                low_priority.append(v2 * v1)
                i += 2
            elif(v == '/'):
                v1 = exp[i + 1]
                v2 = low_priority.pop()
                low_priority.append(int(v2 / v1))
                i += 2
            else:
                low_priority.append(v)
                i += 1

        i = 1
        n = len(low_priority)
        ans = low_priority[0]
        while(i < n):
            sign = low_priority[i]
            v = low_priority[i + 1]
            if(sign == '+'):
                ans += v
            else:
                ans -= v

            i += 2

        return ans


