class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr = [0] + arr
        presum = [0]
        ans = 0
        for i in range(1, len(arr)):
            presum.append(presum[-1] + arr[i])
            k = 1
            while(k <= i):
                ans += (presum[i] - presum[i - k])
                k += 2

        return ans