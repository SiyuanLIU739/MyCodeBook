class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars1, counts1 = self.countchar(word1)
        chars2, counts2 = self.countchar(word2)

        return (chars1 == chars2) and (counts1 == counts2)

    def countchar(self, word1):
        count1 = {}

        for char in word1:
            if char in count1.keys():
                count1[char] += 1
            else:
                count1[char] = 1
        
        chars = []
        counts = []

        for char, count in count1.items():
            chars.append(char)
            counts.append(count)

        chars.sort()
        counts.sort()
        
        return (chars, counts)