class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        mod = 1000000007
        
        queue = [(startRow, startColumn, 0)]
        steps = {(startRow, startColumn, 0): 1}

        deltax = [0, 0, 1, -1]
        deltay = [1, -1, 0, 0]

        while(queue.__len__() != 0):
            x, y, k = queue.pop(0)

            if(x in [-1, m] or y in [-1, n]):
                ans = (ans + steps[(x, y, k)]) % mod
                continue

            if(k == maxMove):
                continue

            for i in range(4):
                xx = x + deltax[i]
                yy = y + deltay[i]

                if(xx < -1 or xx > m or yy < -1 or yy > n):
                    continue

                if((xx, yy, k + 1) not in steps.keys()):
                    steps[(xx, yy, k + 1)] = 0
                steps[(xx, yy, k + 1)] = (steps[(xx, yy, k + 1)] + steps[(x, y, k)]) % mod

                if((xx, yy, k + 1) not in queue):
                    queue.append((xx, yy, k + 1))

        return ans
    