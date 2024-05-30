class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = 0

        pos = {0: 0}

        ans = 0
        i = 0
        for num in nums:
            i += 1
            if(num == 0):
                sums -= 1
            else:
                sums += 1

            if(sums in pos.keys()):
                ans = max(ans, i - pos[sums])
            else:
                pos[sums] = i

        return ans