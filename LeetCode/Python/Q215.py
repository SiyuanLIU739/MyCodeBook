import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)

        smaller = []
        equal = []
        larger = []

        for num in nums:
            if(num < pivot):
                smaller.append(num)
            elif(num == pivot):
                equal.append(num)
            else:
                larger.append(num)
        
        if(k <= len(larger)):
            return self.findKthLargest(larger, k)
        if(k > (len(larger) + len(equal))):
            return self.findKthLargest(smaller, k - len(larger) - len(equal))
        return pivot
    
nums = [3,2,1,5,6,4]
sol = Solution()
sol.findKthLargest(nums, 2)