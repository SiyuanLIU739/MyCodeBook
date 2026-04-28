import random
from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        self.max_weight = 0
        self.w = w
        self.count = []

        count = 0
        for i in range(len(w)):
            count += w[i]
            self.count.append(count)
        
        self.max_weight = count

        
    def pickIndex(self) -> int:
        index = random.randint(1, self.max_weight)

        i = bisect_left(self.count, index)
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()