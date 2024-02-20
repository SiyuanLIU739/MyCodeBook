class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        for i in range(2, len(nums), 3):
            if(nums[i] - nums[i - 2] > k):
                return []
            
        ans = []
        for i in range(0, len(nums), 3):
            ans.append(nums[i: i + 3])

        return ans