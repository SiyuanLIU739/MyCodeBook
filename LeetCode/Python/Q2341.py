class Solution:
    def seekTime(self, garbage, travel, char):
        currentLoc = 0
        ans = 0

        for i in range(len(garbage)):
            if(char in garbage[i]):
                while(currentLoc < i):
                    ans += travel[currentLoc]
                    currentLoc += 1

                ans += garbage[i].count(char)

        return ans
    

    
    def garbageCollection(self, garbage, travel) -> int:
        ans = 0

        for char in "MPG":
            ans += self.seekTime(garbage, travel, char)

        return ans