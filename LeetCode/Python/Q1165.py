class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        last = 0
        ans = 0

        for char in word:
            index = keyboard.find(char)
            ans += abs(index - last)
            last = index

        return ans