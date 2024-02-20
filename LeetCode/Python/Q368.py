class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        f = [1]
        lst = [[nums[0]]]
        ans = []

        for i in range(1, len(nums)):
            f.append(1)
            lst.append([nums[i]])
            for j in range(i):
                if(nums[i] % nums[j] == 0):
                    if(f[j] + 1 > f[i]):
                        f[i] = f[j] + 1
                        lst[i] = lst[j]
                        lst[i].append(nums[i])

                        if(len(lst[i]) > len(ans)):
                            ans = lst[i]

        return ans