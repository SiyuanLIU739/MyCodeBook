class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last1 = -200
        last2 = -200


        dis = len(nums) + 5

        for i in range(len(nums)):
            if(nums[i] == 1):
                dis = min(dis, i - last2)
                last1 = i
            elif(nums[i] == 2):
                dis = min(dis, i - last1)
                last2 = i

        if(dis > len(nums)):
            return -1
        
        return dis

sol = Solution()
nums = [1,0,1,0]
print(sol.minAbsoluteDifference(nums))