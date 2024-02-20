class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1

        ope = 0
        for num in nums:
            if(counts[num] <= 0 or (k - num) not in counts.keys() or counts[k - num] <= 0):
                continue
            ope += 1
            counts[num] -= 1
            counts[k - num] -= 1

            if(counts[num] < 0 or counts[k - num] < 0):
                ope -= 1
            #[3, 3, 3], k = 6

        return ope