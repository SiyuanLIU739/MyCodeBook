class Character:
    def __init__(self, char, order) -> None:
        self.char = char
        self.order = order

    def __lt__(self, other):
        return self.order < other.order
    


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charOrder = {}

        for i in range(len(order)):
            charOrder[order[i]] = i

        string = []
        for char in s:
            if(char in charOrder.keys()):
                string.append(Character(char, charOrder[char]))
            else:
                string.append(Character(char, 100))

        string.sort()

        ans = ""

        for c in string:
            ans += c.char

        return ans
