class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        balloons = [1] + nums + [1]

        f = [[0] * (n + 2) for _ in range(n + 2)]

        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n + 2):
                for last_burst in range(left + 1, right):
                    coins = (f[left][last_burst] + 
                            f[last_burst][right] + 
                            balloons[left] * balloons[last_burst] * balloons[right])
                  
                    f[left][right] = max(f[left][right], coins)

        return f[0][n + 1]