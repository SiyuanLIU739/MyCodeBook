from bisect import bisect_left

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                for c in range(b + 1, len(nums) - 1):
                    t = target - nums[a] - nums[b] - nums[c]
                    if(t < nums[c + 1]):
                        continue
                    if(t not in nums):
                        continue
                    d = bisect_left(nums[c + 1: ], t)
                    ans.add((nums[a], nums[b], nums[c], t))

        ret = []
        for a in ans:
            ret.append([a[0], a[1], a[2], a[3]])

        return ret