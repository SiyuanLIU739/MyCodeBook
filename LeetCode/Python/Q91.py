class Solution:
    def numDecodings(self, s: str) -> int:
        f = [1]

        nums = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
        nums = nums.split(" ")

        s = '0' + s
        for i in range(1, len(s)):
            cnt = 0
            if(s[i] in nums):
                cnt += f[-1]
            if(i - 1 > 0 and s[i - 1: i + 1] in nums):
                cnt += f[-2]
            f.append(cnt)

        return f[-1]