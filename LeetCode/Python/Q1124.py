class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [0] + hours
        presum = [0]
        indexmap = {0: [0]}
        ans = 0

        for i in range(1, len(hours)):
            today = 0
            if(hours[i] > 8):
                today = 1
            else:
                today = -1

            presum.append(presum[-1] + today)

            if(presum[-1] not in indexmap.keys()):
                indexmap[presum[-1]] = []

            indexmap[presum[-1]].append(i)

        sums = sorted(indexmap.keys())

        indexpool = n
        for sum in sums:
            indexes = indexmap[sum]

            if(indexes[-1] > indexpool):
                ans = max(ans, indexes[-1] - indexpool)
            
            indexpool = min(indexpool, indexes[0])

        return ans