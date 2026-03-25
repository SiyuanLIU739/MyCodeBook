class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total = 0
        lineSum = [0] * m
        columnSum = [0] * n

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                lineSum[i] += grid[i][j]
                columnSum[j] += grid[i][j]

        if(total % 2 == 1):
            return False
        
        half = total / 2
        current = 0
        for i in range(m):
            current += lineSum[i]
            if(current == half):
                return True
            if(current > half):
                break

        current = 0
        for j in range(n):
            current += columnSum[j]
            if(current == half):
                return True
            if(current > half):
                break

        return False