class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[-1] + nums[i])
  
        for i in range(len(nums)):
            if(sums[i] == (sums[-1] - sums[i + 1])):
                return i
            
        return -1