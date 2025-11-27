
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0

        freq = {}
        for i in range(len(nums)):
            num = nums[i]
            if(num not in freq.keys()):
                freq[num] = []
            freq[num].append(i)
            degree = max(degree, len(freq[num]))

        ans = len(nums)
        for num in freq.keys():
            if(len(freq[num]) == degree):
                ans = min(ans, freq[num][-1] - freq[num][0] + 1)

        return ans