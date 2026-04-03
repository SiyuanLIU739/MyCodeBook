class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        n = len(isConnected)

        visited = [False] * n

        for i in range(n):
            if(not visited[i]):
                ans += 1
                self.dfs(isConnected, i, n, visited)

        return ans
    
    def dfs(self, isConnected, i, n, visited):
        visited[i] = True

        for j in range(n):
            if(not visited[j] and isConnected[i][j] == 1):
                self.dfs(isConnected, j, n, visited)

        