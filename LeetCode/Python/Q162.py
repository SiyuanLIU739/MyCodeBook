class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if(n == 1):
            return 0
        if(nums[0] > nums[1]):
            return 0
        if(nums[-1] > nums[-2]):
            return n - 1
        
        l = 0
        r = n - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                return mid
            if(nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]):
                l = mid
            else:
                r = mid
        return -1