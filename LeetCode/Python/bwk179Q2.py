from math import comb

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        # left = pos
        # right = n - pos - 1

        # ans = 0
        # for i in range(0, k + 1):
        #     a = i
        #     b = k - i
        #     ans += (comb(left, a) * comb(right, b))

        ans = comb(n - 1, k)

        return (ans * 2) % (1000000000 + 7)
    

sol = Solution()
n = 34
pos = 10
k = 16
print(sol.countVisiblePeople(n, pos, k))
