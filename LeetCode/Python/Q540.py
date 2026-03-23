class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while(l != r):
            mid = (l + r) // 2

            # the side with even elements will contain the single
            if(nums[mid] == nums[mid + 1]):
                left = mid - l + 1
                if(left % 2 == 0):
                    r = mid - 1
                else:
                    l = mid + 2

            # with odd elements 
            else:
                left = mid - l + 1
                if(left % 2 == 1):
                    r = mid
                else:
                    l = mid + 1

        return nums[l]

