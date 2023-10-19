class Q53:
    def findMin(self, nums) -> int:
        return self.find(nums, 0, len(nums) - 1)
    
    def find(self, nums, left, right):
        if(left == right):
            return nums[left]
        
        if(nums[left] < nums[right]):
            return nums[left]
        
        mid = (int)((left + right) / 2)

        if(nums[left] > nums[mid]):
            return self.find(nums, left, mid)
        elif(nums[left] == nums[mid]):
            return self.min(self.find(nums, left, mid), self.find(nums, mid + 1, right))
        return self.find(nums, mid + 1, right)
    
    def min(self, a, b):
        if(a > b):
            return b
        return a
    
    def __init__(self, nums) -> None:
        self.ans = self.findMin(nums)
    
if __name__ == "__main__":
    nums = [2,1,2,2,2]
    ans = Q53(nums)
    print(ans.ans)

