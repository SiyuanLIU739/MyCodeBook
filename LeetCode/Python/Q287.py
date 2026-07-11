class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = int(10e5)

        flag = [False] * n

        for num in nums:
            if(flag[num]):
                return num
            else:
                flag[num] = True

        return n