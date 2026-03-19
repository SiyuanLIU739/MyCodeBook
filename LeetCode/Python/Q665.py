class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        inf = 1000005
        nums.insert(0, -inf)
        nums.append(inf)

        used = False
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i + 1]):
                if(used):
                    return False
                a = nums[i - 1]
                b = nums[i]
                c = nums[i + 1]
                d = nums[i + 2]

                if(a <= c):
                    nums[i] = nums[i - 1]
                elif(b <= d):
                    nums[i + 1] = nums[i]
                else:
                    return False
                used = True

        return True