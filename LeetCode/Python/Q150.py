class Solution:
    def evalRPN(self, tokens) -> int:
        results = []

        for token in tokens:
            if(token not in "+-*/"):
                value = int(token)

                results.append(value)

            else:
                a = results.pop()
                b = results.pop()

                ans = 0

                if(token == '+'):
                    ans = a + b
                elif(token == '-'):
                    ans = b - a
                elif(token == '*'):
                    ans = a * b
                else:
                    ans = b / a

                ans = int(ans)
                results.append(ans)
            
        return results.pop()