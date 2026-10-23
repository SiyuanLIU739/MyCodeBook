class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(n):
            if(k < n):
                k *= 2
            else:
                break
        k -= 1

        sorted_nums = True
        for i in range(n):
            if(nums[i] != i):
                k = k & i
                sorted_nums = False

        if(sorted_nums):
            return 0
        return k