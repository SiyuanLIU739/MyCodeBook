class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int((a ** 2 + b ** 2) ** (1/2))
                if(c > n):
                    continue
                if a ** 2 + b ** 2 == c ** 2:
                    ans += 1

        return ans