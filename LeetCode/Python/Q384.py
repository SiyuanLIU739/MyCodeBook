import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_original = nums.copy()
        self.nums_current = nums.copy()

    def reset(self) -> List[int]:
        self.nums_current = self.nums_original.copy()
        return self.nums_current

    def shuffle(self) -> List[int]:
        n = len(self.nums_current)

        indexes = [i for i in range(n)]
        nums = [0] * n
        i = 0

        while(len(indexes) > 0):
            index = random.choice(indexes)
            indexes.remove(index)
            nums[index] = self.nums_current[i]
            i += 1

        self.nums_current = nums
        return self.nums_current