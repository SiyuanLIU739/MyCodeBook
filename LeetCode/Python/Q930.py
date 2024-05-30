class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum = {0: 1}

        s = 0

        ans = 0
        for num in nums:
            s += num
            seek = s - goal

            if(seek in sum.keys()):
                ans += sum[seek]

            if(s not in sum.keys()):
                sum[s] = 0 
            sum[s] += 1

        return ans