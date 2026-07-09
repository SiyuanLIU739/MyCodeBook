class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        left = -1
        right = -1

        intervals.sort()

        ans = []
        for interval in intervals:
            if(interval[1] >= right):
                if(interval[0] <= right):
                    right = max(right, interval[1])
                else:
                    ans.append([left, right])
                    left = interval[0]
                    right = interval[1]

        ans.append([left, right])
        return ans[1: ]