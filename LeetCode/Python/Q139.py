class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = '0' + s

        f = [False] * len(s)
        f[0] = True

        for i in range(len(s)):
            for word in wordDict:
                st = i - len(word) + 1
                if(st <= 0):
                    continue
                
                if(s[st: i + 1] == word and f[st - 1]): 
                    f[i] = True
                    break

        return f[-1]