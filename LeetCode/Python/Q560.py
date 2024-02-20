class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevMap = {0: 1}
        f = [nums[0]]

        for i in range(1, len(nums)):
            f.append(f[-1] + nums[i])

        ans = 0
        for i in range(len(nums)):
            if(f[i] - k in prevMap.keys()):
                ans += prevMap[f[i] - k]

            if(f[i] not in prevMap.keys()):
                prevMap[f[i]] = 0
            prevMap[f[i]] += 1

        return ans