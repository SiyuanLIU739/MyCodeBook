from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        patterns = defaultdict(list)
        for word in wordSet | {beginWord}:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i+1:]].append(word)

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                if word in wordSet:
                    wordSet.remove(word)

            for word in level:
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in patterns[pattern]:
                        if nei in wordSet:
                            next_level[nei].add(word)
                            if nei == endWord:
                                found = True

            level = next_level
            for k, v in next_level.items():
                parents[k] |= v

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])

        return res