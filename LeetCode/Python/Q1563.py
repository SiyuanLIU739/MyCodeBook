class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        presum = [0]

        for v in stoneValue:
            presum.append(presum[-1] + v)

        n = len(stoneValue)

        f = [[-1] * (n + 1) for _ in range(n + 1)]

        ans = self.findScore(0, n - 1, presum, f)

        return ans

    def findScore(self, l, r, presum, f):
        if(l == r):
            return 0

        if(f[l][r] != -1):
            return f[l][r]

        for k in range(l, r):
            left = presum[k + 1] - presum[l]
            right = presum[r + 1] - presum[k + 1]

            if(left * 2 < f[l][r]):
                continue

            if(right * 2 < f[l][r]):
                break

            ans = 0
            if(left < right):
                ans = self.findScore(l, k, presum, f) + left
            elif(right < left):
                ans = self.findScore(k + 1, r, presum, f) + right
            else:
                ans = max(self.findScore(l, k, presum, f), self.findScore(k + 1, r, presum, f)) + left

            f[l][r] = max(f[l][r], ans)
  
        return f[l][r]