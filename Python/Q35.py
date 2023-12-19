class Solution:
    def search(self, nums, l, r, target):
        if(nums[l] >= target):
            return l - 1
        if(nums[r] < target):
            return r
        
        mid = (l + r) // 2

        if(nums[mid] >= target):
            return self.search(self, nums, l, mid, target)
        if(nums[mid + 1] < target):
            return self.search(self, nums, mid + 1, r, target)
        return mid

    def searchInsert(self, nums, target: int) -> int:
        index = self.search(nums, 0, len(nums) - 1, target)
        return index + 1