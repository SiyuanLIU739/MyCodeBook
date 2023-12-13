class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(1, len(points)):
            ans += self.max(self.abs(points[i][0] - points[i - 1][0]), self.abs(points[i][1] - points[i - 1][1]))

        return ans
    
    def max(self, a, b):
        if(a > b):
            return a
        return b

    def abs(self, x):
        if(x < 0):
            return -x
        return x