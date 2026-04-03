class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if(endWord not in wordList):
            return []

        reach = {beginWord: set()}

        for i in range(len(wordList)):
            if(self.calDistance(beginWord, wordList[i]) == 1):
                reach[beginWord].add(wordList[i])
            if(wordList[i] not in reach.keys()):
                reach[wordList[i]] = set()
            for j in range(i + 1, len(wordList)):
                if(wordList[j] not in reach.keys()):
                    reach[wordList[j]] = set()
                if(self.calDistance(wordList[i], wordList[j]) == 1):
                    reach[wordList[i]].add(wordList[j])
                    reach[wordList[j]].add(wordList[i])

        queue = [[beginWord]]

        ans = []
        while(len(queue) != 0):
            path = queue.pop(0)

            lastWord = path[-1]
            for word in reach[lastWord]:
                if(word in path):
                    continue

                if(word == endWord):
                    # path to be added
                    if(len(ans) == 0 or len(ans[-1]) == len(path) + 1):
                        path.append(word)
                        ans.append(path)
                    # paths in ans to be clear
                    elif(len(ans[-1]) > len(path) + 1):
                        ans = []
                        path.append(word)
                        ans.append(path)
                else:
                    if(len(ans) != 0 and len(path) + 1 >= len(ans[-1])):
                        continue

                    newpath = path.copy()
                    newpath.append(word)
                    queue.append(newpath)

        return ans
    
    def calDistance(self, worda, wordb):
        n = len(worda)

        ans = 0
        for i in range(n):
            if(worda[i] != wordb[i]):
                ans += 1

        return ans