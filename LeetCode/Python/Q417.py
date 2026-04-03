class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])


        visitedPacific = [[False] * n for i in range(m)]
        visitedAtlantic = [[False] * n for i in range(m)]

        pacific = []
        # first line
        for i in range(n):
            pacific.append([0, i])
            visitedPacific[0][i] = True
        # first col
        for i in range(1, m):
            pacific.append([i, 0])
            visitedPacific[i][0] = True

        # bfs
        while(len(pacific) != 0):
            spot = pacific.pop()
            x = spot[0]
            y = spot[1]
            # up
            if(x != 0):
                if(not visitedPacific[x - 1][y] and heights[x - 1][y] >= heights[x][y]):
                    visitedPacific[x - 1][y] = True
                    pacific.append([x - 1, y])
            # down
            if(x + 1 != m):
                if(not visitedPacific[x + 1][y] and heights[x + 1][y] >= heights[x][y]):
                    visitedPacific[x + 1][y] = True
                    pacific.append([x + 1, y])
            # left
            if(y != 0):
                if(not visitedPacific[x][y - 1] and heights[x][y - 1] >= heights[x][y]):
                    visitedPacific[x][y - 1] = True
                    pacific.append([x, y - 1])
            # right
            if(y + 1 != n):
                if(not visitedPacific[x][y + 1] and heights[x][y + 1] >= heights[x][y]):
                    visitedPacific[x][y + 1] = True
                    pacific.append([x, y + 1])

        atlantic = []
        # last line
        for i in range(n):
            atlantic.append([m - 1, i])
            visitedAtlantic[m - 1][i] = True
        # last col
        for i in range(0, m - 1):
            atlantic.append([i, n - 1])
            visitedAtlantic[i][n - 1] = True

        # bfs
        while(len(atlantic) != 0):
            spot = atlantic.pop()
            x = spot[0]
            y = spot[1]
            # up
            if(x != 0):
                if(not visitedAtlantic[x - 1][y] and heights[x - 1][y] >= heights[x][y]):
                    visitedAtlantic[x - 1][y] = True
                    atlantic.append([x - 1, y])
            # down
            if(x + 1 != m):
                if(not visitedAtlantic[x + 1][y] and heights[x + 1][y] >= heights[x][y]):
                    visitedAtlantic[x + 1][y] = True
                    atlantic.append([x + 1, y])
            # left
            if(y != 0):
                if(not visitedAtlantic[x][y - 1] and heights[x][y - 1] >= heights[x][y]):
                    visitedAtlantic[x][y - 1] = True
                    atlantic.append([x, y - 1])
            # right
            if(y + 1 != n):
                if(not visitedAtlantic[x][y + 1] and heights[x][y + 1] >= heights[x][y]):
                    visitedAtlantic[x][y + 1] = True
                    atlantic.append([x, y + 1])

        result = []
        for i in range(m):
            for j in range(n):
                if(visitedAtlantic[i][j] and visitedPacific[i][j]):
                    result.append([i, j])

        return result