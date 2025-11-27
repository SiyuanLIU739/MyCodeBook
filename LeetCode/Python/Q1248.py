from bisect import bisect_left, bisect_right

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        nodd = [0]
        nums = [0] + nums

        for i in range(1, len(nums)):
            nodd.append(nodd[-1] + nums[i] % 2)
            if(nodd[-1] < k):
                continue
            
            t = nodd[-1] - k

            r = bisect_right(nodd, t)
            l = bisect_left(nodd, t)
            ans += (r - l)

        return ans