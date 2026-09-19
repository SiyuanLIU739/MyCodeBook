class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if((xCenter < x1 or xCenter > x2) and (yCenter < y1 or yCenter > y2)):
            disx = min(abs(xCenter - x1), abs(xCenter - x2))
            disy = min(abs(yCenter - y1), abs(yCenter - y2))

            return disx ** 2 + disy ** 2 <= radius ** 2

        if(xCenter < x1 or xCenter > x2):
            return min(abs(xCenter - x1), abs(xCenter - x2)) <= radius

        if(yCenter < y1 or yCenter > y2):
            return min(abs(yCenter - y1), abs(yCenter - y2)) <= radius

        return True