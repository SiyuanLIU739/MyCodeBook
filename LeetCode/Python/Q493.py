from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        sl = SortedList([])

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            ans += sl.bisect_left(num / 2)
            sl.add(num)

        return ans