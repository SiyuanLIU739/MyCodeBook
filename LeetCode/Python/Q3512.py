class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sumnums = 0
        for num in nums:
            sumnums += num

        residual = sumnums % k
        return residual