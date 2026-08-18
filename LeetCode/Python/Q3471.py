class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l = 0
        r = k - 1

        count = {}
        while(r < len(nums)):
            appeared = set(nums[l: r + 1])

            for num in appeared:
                if(num not in count.keys()):
                    count[num] = 0

                count[num] += 1

            l += 1
            r += 1

        ans = -1
        for x in count.keys():
            if(count[x] == 1):
                ans = max(ans, x)

        return ans

            