class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            xUp = x + i
            xDown = x + k - i - 1
            for j in range(k):
                yp = y + j
                tmp = grid[xDown][yp]
                grid[xDown][yp] = grid[xUp][yp]
                grid[xUp][yp] = tmp
        
        return grid