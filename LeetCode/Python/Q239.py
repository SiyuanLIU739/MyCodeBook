class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        swm = []
        for i, num in enumerate(nums):
            if len(dq) > 0 and dq[0] == i - k:
                dq.popleft()
            while len(dq) > 0 and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                swm.append(nums[dq[0]])
        return swm