class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = self.compute(expression)
        return ans
    
    def compute(self, expression):
        signals = False
        for char in expression:
            if(char in '+-*'):
                signals = True
                break

        if(not signals):
            return [int(expression)]
        
        ans = []
        for i in range(len(expression)):
            if(expression[i] in '+-*'):
                left = self.compute(expression[: i])
                right = self.compute(expression[i + 1: ])

                for l in left:
                    for r in right:
                        if(expression[i] == '+'):
                            ans.append(l + r)
                        if(expression[i] == '-'):
                            ans.append(l - r)
                        if(expression[i] == '*'):
                            ans.append(l * r)

        return ans