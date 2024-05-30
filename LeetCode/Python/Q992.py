class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0

        count_num = {}

        r = self.findR(nums, count_num, k, 0, -1)

        if(r == -1):
            return 0
        
        l = 0
        while(r < len(nums)):
            cn = count_num.copy()
            r2 = self.extendR(cn, nums, r)
            count = k

            while(count == k):
                ans += (r2 - r + 1)
                count_num[nums[l]] -= 1

                if(count_num[nums[l]] == 0):
                    count -= 1

                l += 1

            r = self.findR(nums, count_num, k, count, r)

            if(r == -1):
                return ans
            
        return ans


    def findR(self, nums, count_num, k, count, r):
        while(r + 1 < len(nums)):
            r += 1
            if(nums[r] not in count_num.keys() or count_num[nums[r]] == 0):
                count_num[nums[r]] = 0
                count += 1

            count_num[nums[r]] += 1

            if(count == k):
                return r
            
        if(count < k):
            return -1
        
    def extendR(self, count_num, nums, r):
        while(r + 1 < len(nums)):
            r += 1

            if(nums[r] not in count_num.keys() or count_num[nums[r]] == 0):
                return r - 1
            
            count_num[nums[r]] += 1

        return r
