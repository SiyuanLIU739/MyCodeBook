class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        lastHeights = []
        for i in range(m):
            seen = set()
            heights = []
            for lastHeight in lastHeights:
                if(matrix[i][lastHeight[1]] == 1):
                    heights.append((lastHeight[0] + 1, lastHeight[1]))
                    seen.add(lastHeight[1])
            
            for j in range(n):
                if(j in seen): 
                    continue
                if(matrix[i][j] == 1):
                    heights.append((1, j))

            for j in range(len(heights)):
                ans = max(ans, heights[j][0] * (j + 1))
            lastHeights = heights

        return ans