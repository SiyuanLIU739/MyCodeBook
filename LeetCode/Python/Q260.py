class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xs = 0
        for num in nums:
            xs = xs ^ num

        xt = xs & (-xs)
        a = 0
        for num in nums:
            if(num & xt):
                a = a ^ num

        return [a, xs ^ a]