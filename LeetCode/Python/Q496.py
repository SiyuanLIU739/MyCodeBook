class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        nums2 = nums2 + [10000000]
        stack = [n]
        loc = {}

        for i in range(n - 1, -1, -1):
            while(nums2[stack[-1]] <= nums2[i]):
                stack.pop()

            loc[nums2[i]] = stack[-1]
            stack.append(i)

        ans = []
        for num in nums1:
            if(loc[num] == n):
                ans.append(-1)
            else:
                ans.append(nums2[loc[num]])

        return ans