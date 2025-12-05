from bisect import bisect_left, bisect_right

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        ans = 0
        mindiff = 100000

        for l in range(len(nums)):
            if(l != 0 and nums[l] == nums[l - 1]):
                continue
            for r in range(len(nums) - 1, l, -1):
                if(r - l - 1 <= 0):
                    continue
                if(r != len(nums) - 1 and nums[r] == nums[r + 1]):
                    continue

                t = target - nums[l] - nums[r]
                a = bisect_left(nums, t, l + 1, r)
                if(a != r and nums[a] == t):
                    return target
                else:
                    a -= 1
                if(a != l and abs(target - nums[l] - nums[r] - nums[a]) < mindiff):
                    mindiff = abs(target - nums[l] - nums[r] - nums[a])
                    ans = nums[l] + nums[r] + nums[a]
                b = bisect_right(nums, t, l + 1, r)
                if(b != r and abs(target - nums[l] - nums[r] - nums[b]) < mindiff):
                    mindiff = abs(target - nums[l] - nums[r] - nums[b])
                    ans = nums[l] + nums[r] + nums[b]
        return ans