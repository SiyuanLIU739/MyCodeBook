class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        ans = []
        for i in range(len(nums)):
            if(nums[i] == target):
                ans.append(i)
            elif(nums[i] > target):
                break

        return ans