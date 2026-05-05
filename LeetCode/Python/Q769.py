class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = -1

        ans = 0
        for i in range(len(arr)):
            max_seen = max(max_seen, arr[i])
            if(max_seen == i):
                ans += 1

        return ans