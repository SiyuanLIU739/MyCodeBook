class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = []

        for point in points:
            xs.append(point[0])

        xs = sorted(xs)
        ans = 0
        for i in range(1, len(xs)):
            ans = max(ans, xs[i] - xs[i - 1])
        return ans