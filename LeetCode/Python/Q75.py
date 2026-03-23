class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if(num == 0):
                cnt0 += 1
            elif(num == 1):
                cnt1 += 1
            else:
                cnt2 += 1
        
        for i in range(len(nums)):
            if(cnt0 != 0):
                nums[i] = 0
                cnt0 -= 1
            elif(cnt1 != 0):
                nums[i] = 1
                cnt1 -= 1
            else:
                nums[i] = 2
                cnt2 -= 1

        