from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numcount = {}
        for num in nums:
            if(num not in numcount.keys()):
                numcount[num] = 0
            numcount[num] += 1

        if(0 in numcount.keys() and len(numcount) == 1):
            return [[0, 0, 0]]
        nums = sorted(nums)
        ans = set()
        target = 0

        for a in range(len(nums) - 2):
            numcount[nums[a]] -= 1
            for b in range(a + 1, len(nums) - 1):
                numcount[nums[b]] -= 1
                t = target - nums[a] - nums[b]
                if(t >= nums[b + 1] and t in numcount.keys() and numcount[t] > 0):
                    ans.add((nums[a], nums[b], t))
                numcount[nums[b]] += 1
            numcount[nums[a]] += 1

        ret = []
        for a in ans:
            ret.append([a[0], a[1], a[2]])

        return ret