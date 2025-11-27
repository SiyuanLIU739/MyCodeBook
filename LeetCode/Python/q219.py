class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}

        for i in range(len(nums)):
            if(nums[i] not in indexes.keys()):
                indexes[nums[i]] = [i]
            else:
                if(i - indexes[nums[i]][-1] <= k):
                    return True
                indexes[nums[i]].append(i)

        return False