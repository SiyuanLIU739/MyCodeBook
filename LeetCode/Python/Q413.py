class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums.append(-2000)

        st = 0
        ed = 0

        ans = 0
        for i in range(1, len(nums)):
            if(st == ed or nums[st + 1] - nums[st] == nums[i] - nums[i - 1]):
                ed = i
            else:
                n = ed - st + 1
                ans += (1 + n - 2) * (n - 2) // 2
                st = i - 1
                ed = i

        return ans