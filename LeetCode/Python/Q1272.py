class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:
            if(interval[0] >= toBeRemoved[0] and interval[1] <= toBeRemoved[1]):
                continue

            elif(interval[0] >= toBeRemoved[1] or interval[1] <= toBeRemoved[0]):
                ans.append(interval)

            elif(interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]):
                ans.append([interval[0], toBeRemoved[0]])
                ans.append([toBeRemoved[1], interval[1]])
            
            elif(interval[0] < toBeRemoved[1] and interval[1] > toBeRemoved[1]):
                ans.append([toBeRemoved[1], interval[1]])

            elif(interval[1] > toBeRemoved[0]):
                ans.append([interval[0], toBeRemoved[0]])

        return ans