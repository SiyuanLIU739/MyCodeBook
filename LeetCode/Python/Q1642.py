class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        l = 0
        r = len(heights) - 1
        while(l != r):
            mid = (l + r) // 2
            if(self.check(heights, bricks, ladders, mid + 1)):
                l = mid + 1
            else:
                r = mid

        return l
    
    def check(self, heights, bricks, ladders, n):
        dis = []
        for i in range(1, n + 1):
            if(heights[i] <= heights[i - 1]):
                continue
            dis.append(heights[i] - heights[i - 1])

        dis.sort()
        sum = 0
        for i in range(len(dis) - ladders):
            sum += dis[i]
        
        return sum <= bricks