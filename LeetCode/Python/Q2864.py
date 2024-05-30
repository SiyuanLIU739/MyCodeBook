class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt0 = 0
        cnt1 = 1

        for char in s:
            if char == '0':
                cnt0 += 1
            else:
                cnt1 += 1

        ans = 0

        while(cnt1 > 1):
            ans = ans * 2 + 1
            cnt1 -= 1

        while(cnt0 > 0):
            ans = ans * 2
            cnt0 -= 1

        ans = ans * 2 + 1
        return ans