class Solution:
    def minOperations(self, s: str) -> int:
        f = [0, 0]

        for char in s:
            lst = []
            if(char == '0'):
                lst.append(f[1])
                lst.append(f[0] + 1)
            else:
                lst.append(f[1] + 1)
                lst.append(f[0])
            f = lst
        
        return min(f[0], f[1])