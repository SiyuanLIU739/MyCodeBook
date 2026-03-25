class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        ans = 0
        for num in nums:
            if(num - 1 in nums):
                continue
            l = num
            r = num
            while(r + 1 in nums):
                r += 1

            cnt = r - l + 1
            ans = max(ans, cnt)

        return ans