class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)

        cnt = 1
        ans = 0
        for i in range(1, len(nums)):
            if(nums[i] == nums[i - 1]):
                cnt += 1
            else:
                if(cnt == 1):
                    return -1
                ans += int(cnt / 3)
                if(cnt % 3 != 0):
                    ans += 1
                cnt = 1

        if(cnt == 1):
            return -1
        ans += int(cnt / 3)
        if(cnt % 3 != 0):
            ans += 1
        
        return ans