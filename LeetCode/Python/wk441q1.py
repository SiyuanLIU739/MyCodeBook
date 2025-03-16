class Solution:
    def maxSum(self, nums: List[int]) -> int:
        added = set()
        sum = 0
        largest = -10086

        for num in nums:
            if(num > largest):
                largest = num
                
            if(num < 0):
                continue

            if(num in added):
                continue

            sum += num
            added.add(num)

        if(len(added) == 0):
            sum = largest


        return sum