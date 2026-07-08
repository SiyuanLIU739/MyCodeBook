class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = self.rotateSearch(nums, target, 0, n - 1)

        return ans
    
    def rotateSearch(self, nums, target, l, r):
        if(nums[l] == target):
            return l
        if(nums[r] == target):
            return r
        if(l == r or l + 1 == r):
            return -1
        
        mid = (l + r) // 2

        if(nums[l] < nums[mid]):
            # binary search to left
            # rotate search to right
            if(target >= nums[l] and target <= nums[mid]):
                return self.binarySearch(nums, target, l, mid)
            else:
                return self.rotateSearch(nums, target, mid + 1, r)

        else:
            # binary to right
            # rotate to left
            if(target >= nums[mid + 1] and target <= nums[r]):
                return self.binarySearch(nums, target, mid + 1, r)
            else:
                return self.rotateSearch(nums, target, l, mid)
            

    def binarySearch(self, nums, target, l, r):
        if(nums[l] == target):
            return l
        if(nums[r] == target):
            return r
        if(l == r or l + 1 == r):
            return -1
        
        mid = (l + r) // 2

        if(nums[mid] == target):
            return mid
        if(nums[mid] < target):
            return self.binarySearch(nums, target, mid + 1, r)
        return self.binarySearch(nums, target, l, mid)