class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a = ""
        count = 0
        for char in s:
            if(char == '('):
                a += char
                count += 1
            elif(char == ')'):
                if(count == 0):
                    continue
                else:
                    a += char
                    count -= 1
            else:
                a += char
        
        ans = ""
 
        for char in reversed(a):
            if(char == '('):
                if(count > 0):
                    count -= 1
                    continue
                else:
                    ans = char + ans
            else:
                ans = char + ans

        return ans