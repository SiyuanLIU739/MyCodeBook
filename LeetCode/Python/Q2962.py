class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = [-1]

        max = 0
        for num in nums:
            if(num > max):
                max = num

        for i in range(len(nums)):
            if(nums[i] == max):
                pos.append(i)
        pos.append(len(nums))

        if(k + 2 > len(pos)):
            return 0

        ans = 0
        for l in range(1, len(pos)):
            r = l + k - 1
            if(r >= len(pos) - 1):
                break
            ans += (pos[l] - pos[l - 1]) * (pos[-1] - pos[r])
        
        return ans