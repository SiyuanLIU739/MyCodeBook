class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(True):
            try:
                index = nums.index(val)
            except:
                break
            nums.pop(index)

        return len(nums)