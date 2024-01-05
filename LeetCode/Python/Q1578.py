class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(neededTime)

        sum = neededTime[0]
        maxsum = 0
        maxnow = neededTime[0]

        for i in range(1, n):
            sum += neededTime[i]

            if(colors[i] != colors[i - 1]):
                maxsum += maxnow
                maxnow = 0
            
            maxnow = max(maxnow, neededTime[i])

        maxsum += maxnow

        return sum - maxsum