class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for j in range(1, n + 1):
            if(j % 2 == 1):
                ans.append(ans[j >> 1] + 1)
            else:
                ans.append(ans[j >> 1])

        return ans