class Solution:
    def __init__(self):
        print("oh!")

    def search(self, nums, l, r, target):
        if(l > r):
            return [-1, -1]
        
        if(l == r):
            if(nums[l] == target):
                return [l, r]
            else:
                return [-1, -1]
            
        mid = int((l + r) / 2)

        ans = [-1, -1]
        lr1 = [-1, -1]
        lr2 = [-1, -1]

        if(nums[mid] >= target):
            lr1 = self.search(nums, l, mid, target)

        if(nums[mid + 1] <= target):
            lr2 = self.search(nums, mid + 1, r, target)

        if(lr1[0] != -1):
            ans[0] = lr1[0]
        else:
            ans[0] = lr2[0]

        if(lr2[1] != -1):
            ans[1] = lr2[1]
        else:
            ans[1] = lr1[1]

        return ans


    def searchRange(self, nums, target: int):
        return self.search(nums, 0, len(nums) - 1, target)


nums = []
t = 6
sol = Solution()
print(sol.searchRange(nums, t))