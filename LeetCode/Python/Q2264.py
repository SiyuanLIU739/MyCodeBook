class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        for i in range(2, len(num)):
            if(num[i - 2] == num[i - 1] and num[i - 1] == num[i]):
                if(ans < num[i - 2: i + 1]):
                    ans = num[i - 2: i + 1]

        return ans