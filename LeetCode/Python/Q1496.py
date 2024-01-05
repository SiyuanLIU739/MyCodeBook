class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        points = [(x, y)]

        how = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for d in path:
            h = how[d]
            x += h[0]
            y += h[1]

            if((x, y) in points):
                return True
            points.append((x, y))

        return False

