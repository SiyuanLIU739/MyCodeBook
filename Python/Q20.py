class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char not in mapping.keys():
                stack.append(char)

            else:
                lst = stack.pop()
                if(mapping.get(char) != lst):
                    return False
        
        return len(stack) == 0