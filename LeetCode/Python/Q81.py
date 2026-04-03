from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        return self.binary(nums, 0, n - 1, target)
    
    def binary(self, nums, l, r, target):
        if(l == r):
            return nums[l] == target
        
        mid = (l + r) // 2

        if(nums[l] < nums[mid]):
            if(target >= nums[l] and target <= nums[mid]):
                index = bisect_left(nums, target, l, mid + 1)
                return nums[index] == target
            return self.binary(nums, mid + 1, r, target)
        elif(nums[mid] < nums[r]):
            if(target >= nums[mid] and target <= nums[r]):
                index = bisect_left(nums, target, mid, r + 1)
                return nums[index] == target
            return self.binary(nums, l, mid, target)
        else:
            result = self.binary(nums, l, mid, target)
            if(result):
                return result
            return self.binary(nums, mid + 1, r, target)