class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        rt = self.tree

        for char in word:
            if(char not in rt.keys()):
                rt[char] = {}
            rt = rt[char]
        
        rt['.'] = True

    def search(self, word: str) -> bool:
        rt = self.tree

        for char in word:
            if(char not in rt.keys()):
                return False
            rt = rt[char]

        return '.' in rt.keys()

    def startsWith(self, prefix: str) -> bool:
        rt = self.tree

        for char in prefix:
            if(char not in rt.keys()):
                return False
            rt = rt[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)