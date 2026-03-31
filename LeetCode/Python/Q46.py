from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permu = permutations(nums)

        ret = [list(p) for p in permu]

        return ret