class Solution:
    def maxProduct(self, words: List[str]) -> int:
        letters = []

        for word in words:
            letter = 0
            for char in word:
                letter = letter | (1 << (ord(char) - ord('a')))
            letters.append(letter)

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if(letters[i] & letters[j] == 0):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans