class Solution:
    def trailingZeroes(self, n: int) -> int:
        n2 = 0
        n5 = 0

        for i in range(1, n + 1):
            n2 += self.count2(i)
            n5 += self.count5(i)

        return min(n2, n5)
    
    def count2(self, x):
        cnt = 0
        while(x % 2 == 0):
            cnt += 1
            x = x // 2
        return cnt
    
    def count5(self, x):
        cnt = 0
        while(x % 5 == 0):
            cnt += 1
            x = x // 5
        return cnt