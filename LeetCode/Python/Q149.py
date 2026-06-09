class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points) == 1):
            return 1

        lines = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]

                if(x1 == x2):
                    lines[(x1)] = 0
                else:
                    a = (y1 - y2) * 1.0 / (x1 - x2)
                    b = y1 - a * x1
                    lines[(a, b)] = 0

        ans = 0
        eps = 0.000001
        for point in points:
            for line in lines.keys():
                if(type(line) == type(1)):
                    if(line == point[0]):
                        lines[line] += 1
                else:
                    a = line[0]
                    b = line[1]
                    yprime = a * point[0] + b
                    if(abs(yprime - point[1]) < eps):
                        lines[line] += 1

                ans = max(ans, lines[line])


        return ans