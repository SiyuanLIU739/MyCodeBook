class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0

        cmp = x ^ y

        while(cmp != 0):
            if(cmp % 2 == 1):
                ans += 1
            cmp = cmp >> 1

        return ans