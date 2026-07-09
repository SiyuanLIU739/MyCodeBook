class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        i = n * 2 - 1
        q = []
        while(i > 0):
            while(q and q[-1] <= nums[i % n]):
                q.pop()
            
            if(q):
                ans[i % n] = q[-1]
            
            q.append(nums[i % n])

            i -= 1

        return ans