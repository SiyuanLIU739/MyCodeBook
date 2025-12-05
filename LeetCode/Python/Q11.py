class Bar:
    def __init__(self, height, index) -> None:
        self.height = height
        self.index = index

    def __lt__(self, other):
        if(other.height == self.height):
            return self.index > other.index
        return self.height < other.height

class Solution:
    def maxArea(self, height: List[int]) -> int:
        bars = []
        for i in range(len(height)):
            bars.append(Bar(height[i], i))
        bars.sort()

        maxi = len(height) - 1
        ans = 0
        mini = maxi
        for i in range(len(height) - 2, -1, -1):
            ans = max(ans, bars[i].height * max(abs(bars[i].index - maxi), abs(bars[i].index - mini)))
            if(bars[i].index < mini):
                mini = bars[i].index
            if(bars[i].index > maxi):
                maxi = bars[i].index
        
        return ans
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        positions = {}
        for i in range(len(height)):
            if(height[i] not in positions.keys()):
                positions[height[i]] = []
            positions[height[i]].append(i)

        heights = sorted(positions.keys(), reverse = True)

        maxi = -1
        mini = len(height)
        ans = 0

        for h in heights:
            maxi = max(maxi, positions[h][-1])
            mini = min(mini, positions[h][0])
            ans = max(ans, (maxi - mini) * min(height[maxi], height[mini]))

        return ans