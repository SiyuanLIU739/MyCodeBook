class Char:
    def __init__(self, char) -> None:
        self.c = char
        self.f = 0

    def add(self):
        self.f += 1

    def __lt__(self, other):
        return self.f < other.f
    


class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}

        for char in s:
            if(char not in chars.keys()):
                chars[char] = Char(char)
            
            chars[char].add()

        candidate = []
        for key, item in chars.items():
            candidate.append(item)

        candidate.sort(reverse = True)

        ans = ""
        for c in candidate:
            ans += c.c * c.f
        
        return ans