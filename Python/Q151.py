class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")

        ans = ""

        for str in lst:
            if(str == ''):
                continue
            ans = str + " " + ans

        return ans[: -1]