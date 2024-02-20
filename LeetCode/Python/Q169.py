class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]

        l = 0
        r = 1

        while(r < n):
            if(nums[l] == nums[r]):
                r += 1
            else:
                nums[r] = 1.1e9
                l += 1
                while(l < n and abs(nums[l] - 1.1e9) < 1):
                    l += 1

                if(l > r):
                    r = l + 1
                else:
                    r += 1

        return nums[l] 