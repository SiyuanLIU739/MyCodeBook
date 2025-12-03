class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 1

        while(i * i <= n):
            i += 1
        
        return i - 1