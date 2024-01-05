class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        cnt = 0
        ans = [[nums[0]]]

        for i in range(1, len(nums)):
            if(nums[i] != nums[i - 1]):
                cnt = -1
            
            cnt += 1
            if(cnt >= len(ans)):
                ans.append([])
            ans[cnt].append(nums[i])

        return ans