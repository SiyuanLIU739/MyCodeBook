class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNum = 0

        for num in nums:
            sumNum += num

        if(sumNum % 2 == 1):
            return False
        
        target = sumNum // 2
        f = [True] + [False] * target

        for num in nums:
            for j in range(target, -1, -1):
                if(j - num < 0):
                    break
                if(f[j - num]):
                    f[j] = True

        return f[target]