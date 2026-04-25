class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last = {0: 1}
        f = {}

        for num in nums:
            for key, value in last.items():
                if(key + num not in f.keys()):
                    f[key + num] = value
                else:
                    f[key + num] += value

                if(key - num not in f.keys()):
                    f[key - num] = value
                else:
                    f[key - num] += value

            last = f
            f = {}

        if(target not in last.keys()):
            return 0
        return last[target]