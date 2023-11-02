class Solution:
    def spiralOrder(self, matrix):
        ans = []

        m = len(matrix)
        n = len(matrix[0])

        flags = []
        for i in range(m):
            flags.append([])
            for j in range(n):
                flags[i].append(False)

        direction_x = [0, 1, 0, -1]
        direction_y = [1, 0, -1, 0]


        next_x = 0
        next_y = 0
        dir = 0

        while(next_x != None):
            x = next_x
            y = next_y

            next_x = None
            next_y = None

            ans.append(matrix[x][y])
            flags[x][y] = True

            j = 0
            while(j < 4):
                potential_x = x + direction_x[dir]
                potential_y = y + direction_y[dir]

                if(
                    (potential_x < 0) or 
                    (potential_x >= m) or 
                    (potential_y < 0) or 
                    (potential_y >= n) or 
                    (flags[potential_x][potential_y])
                ):
                    j += 1
                    dir += 1
                    dir %= 4
                else:
                    next_x = potential_x
                    next_y = potential_y
                    break

        return ans