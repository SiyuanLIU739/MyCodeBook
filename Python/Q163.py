class Solution:
    def findMissingRanges(self, nums, lower, upper):
        ans = []

        nums.insert(0, lower - 1)
        nums.append(upper + 1)

        for i in range(1, len(nums)):
            left = nums[i - 1] + 1
            right = nums[i] - 1

            if(right <= left):
                continue

            ans.append([left, right])

        return ans
        