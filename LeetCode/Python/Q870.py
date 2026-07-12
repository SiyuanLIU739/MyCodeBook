class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort(key = lambda x: -x)

        nums2_pos = {}
        for i in range(n):
            if(nums2[i] not in nums2_pos.keys()):
                nums2_pos[nums2[i]] = []
            nums2_pos[nums2[i]].append(i)
        nums2.sort(key = lambda x: -x)

        i = 0
        j = 0
        ans = [-1] * n
        while(i < n and j < n):
            while(j < n and nums1[i] <= nums2[j]):
                j += 1
            
            if(j == n):
                break
            
            for pos in nums2_pos[nums2[j]]:
                if(ans[pos] < 0):
                    ans[pos] = nums1[i]
                    break
            i += 1
            j += 1

        j = 0
        while(i < n and j < n):
            while(j < n and ans[j] >= 0):
                j += 1
            if(j == n):
                break
            
            ans[j] = nums1[i]
            i += 1
            j += 1

        return ans